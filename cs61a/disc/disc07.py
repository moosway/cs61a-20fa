class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, staff):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)
class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1
        
callahan = Professor("Callahan")
elle = Student("Elle", callahan)
elle.visit_office_hours(callahan)
elle.visit_office_hours(Professor("Paulette"))
elle.understanding
[name for name in callahan.students]
x = Student("Vivian", Professor("Stromwell")).name
x
[name for name in callahan.students]

class MinList:
    """A list that can only pop the smallest element """
    def __init__(self):
        self.items = []
        self.size = 0
    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items+=[item]
        self.size+=1
    def pop(self):
        """ Removes and returns the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        minnum=min(self.items)
        for i in range(self.size):
            if self.items[i]==minnum:
                self.items=self.items[0:i]+self.items[i+1:]
                self.size-=1
                return minnum
            
m = MinList()
m.append(4)
m.append(2)
m.size
m = MinList()
m.append(4)
m.append(1)
m.append(5)
m.pop()
m.size

class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg=msg
        self.sender_name=sender_name
        self.recipient_name=recipient_name
        
        
class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}
        
    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        if email.recipient_name in self.client:
            self.clients[email.recipient_name].receive(email)
    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name]=client
        
class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server=server
        self.name=name
    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        self.server.send(Email(msg,self,recipient_name))
    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox+=[email]
        
'''        
class Dog():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name + " says woof!")
class Cat():
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name + " says meow!")
'''
       
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)
class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self,name,owner)
        self.lives=lives
        self.is_alive = True if self.lives > 0 else False
    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + " says meow!")
    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if self.lives>0:
            self.lives-=1
            self.is_alive=False if not self.lives else True
        else:
            print('the cat has no more lives to lose.')
            
class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not? no
        Cat.__init__(self,name,owner,lives)
    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        print('{} says meow!'.format(self.name))
    def __repr__(self):
        """The interpreter-readable representation of a NoisyCat
        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoisyCat('Muffin', 'Catherine')"""
        return "NoisyCat('{}','{}')".format(self.name,self.owner)
        
    
        
muffin = NoisyCat("Muffin", "Catherine")
muffin.__repr__()