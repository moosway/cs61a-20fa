"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    p=[paragraphs[i] for i in range(0,len(paragraphs)) if select(paragraphs[i])]
    if k<len(p):
        return p[k]
    return ''
    # END PROBLEM 1

def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2            
    def bool(pa,i=0):
        if i==len(topic):
            return False
        if topic[i]==pa:
            return True
        return bool(pa,i+1)    

    def re(pa):
        def fen(yf,i=0):#pa中第i个词
            if i==len(yf):
                return False
            if bool(yf[i]):
                return bool(yf[i])
            else:
                return fen(yf,i+1)
        return fen(split(lower(remove_punctuation(pa))))
    return re
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    def con(typed,ref,i=0,n=0):
        if len(typed)==0:
            return 0.0
        if i==min(len(typed),len(ref)):
            return n/len(typed)*100
        if typed[i]==ref[i]:
            return con(typed,ref,i+1,n+1)
        return con(typed,ref,i+1,n)    
    return con(typed_words,reference_words)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    if len(typed)==0:
        return 0.0
    return len(typed)/5/elapsed*60
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    mini=0
    for i in range(0,len(valid_words)):
        if user_word==valid_words[i]:
            return user_word
        if diff_function(user_word,valid_words[i],limit)<diff_function(user_word,valid_words[mini],limit):
            mini=i
        i=i+1
    if diff_function(user_word,valid_words[mini],limit)>limit:
        return user_word
    return valid_words[mini]
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def diff(start,goal,limit,i=0,j=0):
        if i==min(len(start),len(goal)) or j>limit:
            return j+abs(len(goal)-len(start))
        if start[i]==goal[i]:
            return diff(start,goal,limit,i+1,j)
        return diff(start,goal,limit,i+1,j+1)
    return diff(start, goal, limit)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    def paw(start,goal,limit,i,j):
        if i>=min(len(start),len(goal)) or j>limit: # Fill in the condition
            return j+abs(len(goal)-len(start))
        elif start[i]==goal[i]: # Feel free to remove or add additional cases
            # BEGIn
            return paw(start[(i+1):],goal[(i+1):],limit,0,j)
            # END
        else:
            add_diff = paw(goal[i]+start[i:],goal[i:],limit,0,j+1)
            remove_diff = paw(start[(i+1):],goal[i:],limit,0,j+1)
            substitute_diff = paw(goal[i]+start[(i+1):],goal[i:],limit,0,j+1)
            # BEGIN
            return min(add_diff,remove_diff,substitute_diff)
            # END
    return paw(start,goal,limit,0,0)

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########

def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8   
    def word(typed,prompt,i,j):
        if i==len(typed):
            send({'id': user_id, 'progress': j/len(prompt)})
            return j/len(prompt)    
        elif typed[i]==prompt[i]:
            return word(typed,prompt,i+1,j+1)
        send({'id': user_id, 'progress': j/len(prompt)})
        return j/len(prompt)
    return word(typed,prompt,0,0)
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report
         #   print([words,timegaped])

def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    timegaped=[[1 for i in range(len(words))]for j in range(len(times_per_player))]
    def timegap(player,timegaped):
        if player==len(times_per_player):
            return game(words,timegaped)
        def jian(i,timegaped):
            if i==len(words):
                return timegap(player+1,timegaped)
            timegaped[player][i]=times_per_player[player][i+1]-times_per_player[player][i]
            return jian(i+1,timegaped)
        return jian(0,timegaped)    
    return timegap(0,timegaped)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    wordlist=[[]for i in player_indices]
    def con(i):
        if i==len(all_words(game)):
            return wordlist
        def player(j,m):
            if j==len(all_times(game))-1:
                wordlist[m].append(all_words(game)[i])
                return con(i+1)
            if all_times(game)[m][i]>all_times(game)[j+1][i]:
                m=j+1
            return player(j+1,m)
        return player(0,0)
    return con(0)
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)