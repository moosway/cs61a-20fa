class A():
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return self.x
    def __str__(self):
        return self.x * 2
    
class B():
    def __init__(self):
        print("boo!")
        self.a = []
    def add_a(self, a):
        self.a.append(a)
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret
a=A('one')
print(A("one"))
repr(A("two"))
b=B()
b.add_a(A("a"))
b.add_a(A("b"))
b

def a(t):
    return t
s='aa'
print(a(s))

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest==Link.empty:
        return lnk.first
    return lnk.first+sum_nums(lnk.rest)
a = Link(1, Link(6, Link(7)))
sum_nums(a)

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    s,whi = 1,True
    for i in range(len(lst_of_lnks)):
        if lst_of_lnks[i].rest==Link.empty:
            whi=False
        else:
            whi=whi and True
        s=s*lst_of_lnks[i].first
        lst_of_lnks[i]=lst_of_lnks[i].rest
    if whi:
        return Link(s,multiply_lnks(lst_of_lnks))
    return Link(s)
a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])
p.first
p.rest.first
p.rest.rest.rest is Link.empty           

def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk!=Link.empty and lnk.rest!=Link.empty:
        lnk.first,lnk.rest.first=lnk.rest.first,lnk.first   
        flip_two(lnk.rest.rest)

one_lnk = Link(1)
flip_two(one_lnk)
one_lnk
lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
flip_two(lnk)
lnk



def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link!=Link.empty:
        if f(link.first):
            yield link.first
        link=link.rest
link = Link(1, Link(2, Link(3)))
g = filter_link(link, lambda x: x % 2 == 0)
next(g)
next(g)
list(filter_link(link, lambda x: x % 2 != 0))

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches
    
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label%2:
        t.label+=1
    for branch in t.branches:
        make_even(branch)
t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
make_even(t)
t.label
t.branches[0].branches[0].label

def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    t.label**=2
    for branch in t.branches:
        square_tree(branch)
t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
square_tree(t)
t.label
t.branches[0].label
t.branches[2].label
t.branches[0].branches[0].label

def find_paths(t, entry):
    '''
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    '''
    paths = []
    br=0
    if t.label==entry:
        return [t.label]
    for branch in t.branches:
        if find_paths(branch,entry):
            br+=1
            if br==1:
                if isinstance(find_paths(branch,entry)[0], list):
                    [paths.append([t.label]+i) for i in find_paths(branch,entry)]
                else:
                    paths+=[t.label]+find_paths(branch,entry)
            else:
                if isinstance(paths[0], list)==False:
                    paths=[paths]
                if isinstance(find_paths(branch,entry)[0], list):
                    [paths.append([t.label]+i) for i in find_paths(branch,entry)]
                else:
                    paths.append([t.label]+find_paths(branch,entry))
                
    return paths      
    '''
    for branch in t.branches:
        if find_paths(branch,entry):
            paths.append([t.label]+ find_paths(branch,entry))
    return paths
    '''
tree_ex = Tree(2, [Tree(7, [Tree(5), Tree(6, [Tree(5), Tree(5)])]), Tree(1, [Tree(5)])])
find_paths(tree_ex, 5)
find_paths(tree_ex, 12)
paths=[[1,2]]

    
isinstance(paths[0], list)

def mul(a,b):
    return a*b


def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    if t1.branches!=[] and t2.branches!=[]:
        branches=list(zip(t1.branches,t2.branches))
        return Tree(combiner(t1.label,t2.label),[combine_tree(branch[0],branch[1],combiner) for branch in branches])
    return Tree(combiner(t1.label,t2.label))

a = Tree(1, [Tree(2, [Tree(3)])])
b = Tree(4, [Tree(5, [Tree(6)])])
combined = combine_tree(a, b, mul)
combined.label
combined.branches[0].label
        
def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    if t.branches!=[]:
        return Tree(map_fn(t.label),[Tree(branch.label,[alt_tree_map(branc,map_fn) for branc in branch.branches]) for branch in t.branches])
    return Tree(map_fn(t.label))
t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
negate = lambda x: -x
tt=alt_tree_map(t, negate)
tt.label
tt.branches[0].label
tt.branches[1].label
tt.branches[0].branches[0].label