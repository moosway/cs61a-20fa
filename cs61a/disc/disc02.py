def is_even(x):
     # Even numbers have remainder 0 when divided by 2.
    return x % 2 == 0

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true

    >>> 
    2
    4
    """
    for i in range(1,n+1):
        if is_even(i):
            print(i)

#keep_ints(is_even, 5)

def make_keeper(n):
    def tf(cond):
        for i in range(1,n+1):
            if cond(i):
                print(i)
    return tf

make_keeper(5)(is_even)

n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
   return f(x + n)

f = f(g, n)
print((lambda y: y())(f))

y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        return y + "i"
    y = lambda y: y(h)
    return lambda h: y(h)
print(y(y)(y))

def print_delayed(x):
    """Return a new function. This new function, when called,
will print out x and return another function with the same
behavior.
>>> f = print_delayed(1)
>>> f = f(2)
1
>>> f = f(3)
2
>>> f = f(4)(5)
3
4
>>> f("hi")
5
<function print_delayed> # a function is returned
"""
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

f = print_delayed(1)
print(f(2)(3)('hi')(4))


def print_n(n):
    """
>>> f = print_n(2)
>>> f = f("hi")
hi
>>> f = f("hello")
hello
>>> f = f("bye")
done
>>> g = print_n(1)
>>> g("first")("second")("third")
first
done
done
<function inner_print>
"""
    def inner_print(x):
        if n<=0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print

f=print_n(3)
print(f(2)(4)('hi')(5))