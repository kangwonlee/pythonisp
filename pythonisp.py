# Reference
# John McCarthy et. al., LISP 1.5 Programmer's Manual, Second Edition, The MIT Press, ISBN 0 262 13011 4

def cons(a, b):
     return a, b


def car(a):
     assert isinstance(a, (list, tuple)), f'undefinded for {repr(a)}'
     assert 2 == len(a), f'undefinded for {repr(a)}'
     return a[0]


def cdr(a):
     assert isinstance(a, (list, tuple)), f'undefinded for {repr(a)}'
     assert 2 == len(a), f'undefinded for {repr(a)}'
     return a[1]


def eq(a, b):
     assert not isinstance(a, (list, tuple)), f'undefinded for {repr(a)}'
     assert not isinstance(b, (list, tuple)), f'undefinded for {repr(b)}'

     return a == b


def atom(a):
     return isinstance(a, str)


def lst(*arg):
     assert arg, f'undefinded for {repr(arg)}'
     if 1 == len(arg):
          result = (arg[0], False)
     elif 2 == len(arg):
          result = (arg[0], lst(arg[1]))
     elif 2 < len(arg):
          result = (arg[0], lst(*arg[1:]))
     else:
          raise NotImplementedError
     
     return result
