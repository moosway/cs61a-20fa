def multiply(m, n):
    """
>>> multiply(5, 3)
15
"""
    if n>1:
        return m+multiply(m,n-1)
    return m

multiply(5, 3)

def rec(x, y):
    if y > 0:
        return x * rec(x, y - 1)
    return 1
rec(3, 4)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
number of elements in the sequence.
>>> a = hailstone(10)
10
5
16
8
4
2
1
>>> a
7
"""
    m=1
    def stone(n,i):
        print(n)
        if n%2==0:
            return stone(n//2,i+1)
        elif n==1:
            return i
        return stone(n*3+1,i+1)
    return stone(n,m)

print(hailstone(10))


def merge1(n1, n2):
    """ Merges two numbers
>>> merge(31, 42)
4321
>>> merge(21, 0)
21
>>> merge (21, 31)
3211
"""
    i=0
    def h(n1,n2,i):
        if n1>0 and n2>0:
            a=n1%10
            b=n2%10
            if a==0:
                return (b*10**i+h(n1//10,n2//10,i+1))
            elif b==0:
                return (a*10**i+h(n1//10,n2//10,i+1))
            elif b<a:
                return (b*10**i+h(n1,n2//10,i+1))
            return (a*10**i+h(n1//10,n2,i+1))
        elif n1==0:
            return n2*10**i
        return n1*10**i
    return h(n1,n2,i)



def merge(n1,n2):
    if n1 == 0 and n2:
        return n2
    elif n2 == 0 and n1:
        return n1
    elif n1%10==0:
        return merge(n1//10,n2//10)*10+n2%10
    elif n2%10==0:
        return merge(n1//10,n2//10)*10+n1%10
    elif n1 % 10 <= n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10


print(merge(31, 530))


def make_func_repeater(f, x):
    """
>>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
>>> incr_1(2) #same as f(f(x))
3
>>> incr_1(5)
6
"""
    def repeat(y):
        if y==0:
            return x
        else:
            return f(repeat(y-1))
    return repeat

incr_1 = make_func_repeater(lambda x: x + 1, 1)
print(incr_1(8)) #same as f(f(x))

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(y):
        if n==1:
            return False
        elif n==2:
            return True
        else:
            if n%y==0:
                return False
            elif y==2:
                return True
            return prime_helper(y-1)
    return prime_helper(n-1)

print(is_prime(20))