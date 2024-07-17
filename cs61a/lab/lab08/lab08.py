def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    stri=[]
    while link!=Link.empty:
        stri+=[link.first]
        link=link.rest
    return stri

def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
    if s != Link.empty and s.rest != Link.empty:
        every_other(s.rest.rest)
        s.rest= s.rest.rest
    elif s != Link.empty:
        s.rest=Link.empty
    '''
    while s != Link.empty and s.rest != Link.empty:
        s.rest = s.rest.rest#这个可以改变到外面
        s = s.rest#这个改变不到外面
    '''
    '''

    def js(p):
        if p.rest!=Link.empty and p.rest.rest!=Link.empty:
            return Link(p.first,js(p.rest.rest))
        return Link(p.first)
    if s.rest==Link.empty or s.rest.rest==Link.empty:
        s.rest=Link.empty
    else:
        s.rest=js(s.rest.rest)
    #不能直接改变s,但是可以直接改变s.rest,i mean参数传递不到函数外面
    #就像数列,可以改变元素,但不能直接变整体
    
    a=[1,2,3]
    def pp(a):
        a[0]=2
        a=[2]
    pp(a)
    a
    '''
def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    for branch in t.branches:
        cumulative_mul(branch)
        t.label=t.label*branch.label


def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    
    seen = []
    cur_link = link
    while cur_link != Link.empty:
        if cur_link in seen:
            return True
        seen.append(cur_link)
        cur_link = cur_link.rest
    return False

    '''
    try:
        while link.rest!=Link.empty:
            link=link.rest
        return False
    except Exception:
        return True
        
    '''


    
def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return False

    slow, fast = link, link.rest

    while fast is not Link.empty:
        if fast.rest == Link.empty:
            return False
        elif fast == slow or fast.rest == slow:
            return True
        else:
            slow, fast = slow.rest, fast.rest.rest
    return False
    '''
    try:
        while link:
            ret
    except RecursionError:
        return True
'''

def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    s=[]
    for branch in t.branches:
        s+=[branch.label]
    i=0
    for branch in t.branches:
        branch.label=s[len(s)-i-1]
        i+=1
        for branc in branch.branches:
            reverse_other(branc)
 
    


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
'''
>>> from lab09 import *
>>> link = Link(1000)
>>> link.first
? 1000
-- OK! --

>>> link.rest is Link.empty
? True
-- OK! --

>>> link = Link(1000, 2000)
? Error
-- OK! --

>>> link = Link(1000, Link())
? Error
-- OK! --

>>> link = Link(1, Link(2, Link(3)))
>>> link.first
? 1
-- OK! --

>>> link.rest.first
? 2
-- OK! --

>>> link.rest.rest.rest is Link.empty
? True
-- OK! --

>>> link.first = 9001
>>> link.first
? 9001
-- OK! --

>>> link.rest = link.rest.rest
>>> link.rest.first
? 3
-- OK! --

>>> link = Link(1)
>>> link.rest = link
>>> link.rest.rest.rest.rest.first
? 1
-- OK! --

>>> link = Link(2, Link(3, Link(4)))
>>> link2 = Link(1, link)
>>> link2.first
? 1
-- OK! --

>>> link2.rest.first
? 2
-- OK! --

>>> link = Link(5, Link(6, Link(7)))
>>> link                  # Look at the __repr__ method of Link
? Link(5, Link(6, Link(7)))
-- OK! --

>>> print(link)          # Look at the __str__ method of Link
? <5 6 7>
-- OK! --
'''

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

