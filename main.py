# Reference
# John McCarthy et. al., LISP 1.5 Programmer's Manual, Second Edition, The MIT Press, ISBN 0 262 13011 4

def cons(a, b):
     return a, b


def car(a):
    assert isinstance(a, (list, tuple))
    assert 2 == len(a), repr(a)
    return a[0]


def cdr(a):
    assert isinstance(a, (list, tuple))
    assert 2 == len(a), repr(a)
    return a[1]
