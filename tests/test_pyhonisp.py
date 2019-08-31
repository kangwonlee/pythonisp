# Reference
# John McCarthy et. al., LISP 1.5 Programmer's Manual, Second Edition, The MIT Press, ISBN 0 262 13011 4

import os
import sys

import pytest


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            os.pardir
        )
    )
)


import pythonisp


def test_cons():
    assert ('A', 'B') == pythonisp.cons('A', 'B')
    assert (('A', 'B'), 'C') == pythonisp.cons(('A', 'B'), 'C')


def test_car():
    assert 'A' == pythonisp.car(('A', 'B'))
    assert 'A' == pythonisp.car(('A', ('B1', 'B2')))
    assert ('A1', 'A2') == pythonisp.car((('A1', 'A2'), 'B'))


def test_cdr():
    assert 'B' == pythonisp.cdr(('A', 'B'))
    assert ('B1', 'B2') == pythonisp.cdr(('A', ('B1', 'B2')))
    assert 'B' == pythonisp.cdr((('A1', 'A2'), 'B'))

    assert pythonisp.cdr(('A', ('B1', 'B2')))

if "__main__" == __name__:
    pytest.main()
