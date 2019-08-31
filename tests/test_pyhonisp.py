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

    # https://doc.pytest.org/en/latest/assert.html
    with pytest.raises(AssertionError) as exinfo:
        pythonisp.car('A')
    assert 'undefinded' in str(exinfo.value)


def test_cdr():
    assert 'B' == pythonisp.cdr(('A', 'B'))
    assert ('B1', 'B2') == pythonisp.cdr(('A', ('B1', 'B2')))
    assert 'B' == pythonisp.cdr((('A1', 'A2'), 'B'))

    assert 'B1' == pythonisp.car(pythonisp.cdr(('A', ('B1', 'B2'))))
    assert 'A' == pythonisp.car(pythonisp.cons('A', 'B1'))

    # https://doc.pytest.org/en/latest/assert.html
    with pytest.raises(AssertionError) as exinfo:
        pythonisp.cdr('A')
    assert 'undefinded' in str(exinfo.value)

    with pytest.raises(AssertionError) as exinfo:
        pythonisp.car(pythonisp.cdr('A'))
    assert 'undefinded' in str(exinfo.value)


def test_cons_car_cdr():
    assert 'x' == pythonisp.car(pythonisp.cons('x', 'y'))
    assert 'y' == pythonisp.cdr(pythonisp.cons('x', 'y'))


def test_eq():
    assert pythonisp.eq('A', 'A')
    assert not pythonisp.eq('A', 'B')

    with pytest.raises(AssertionError) as exinfo:
        pythonisp.eq('A', ('A', 'B'))
    assert 'undefinded' in str(exinfo.value)

    with pytest.raises(AssertionError) as exinfo:
        pythonisp.eq(('A', 'B'), ('A', 'B'))
    assert 'undefinded' in str(exinfo.value)


def test_atom():
    assert pythonisp.atom('AVERYLONGSTRING')
    assert not pythonisp.atom(('U', 'V'))
    assert pythonisp.atom(pythonisp.car(('U', 'V')))


def test_lst_ab():
    result = pythonisp.lst('A', 'B')
    expected = ('A', ('B', False))

    assert expected == result


def test_lst_abc():
    result = pythonisp.lst('A', 'B', 'C')
    expected = (
        'A', (
            'B', (
                'C', False
            )
        )
    )

    assert expected == result


def test_lst_ab_c():
    result = pythonisp.lst(('A', 'B'), 'C')
    expected = (('A', ('B', False), ('C', False)))

    assert expected == result


if "__main__" == __name__:
    pytest.main()
