# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from funcs import (
    prod,
    prod2,
    longest,
    dist
)


def test_prod():
    assert prod(1, 2, 3) == 6
    assert prod(0, 1, 2) == 0
    assert prod(1, -2, 5) == -10



def test_prod2():
    #Test should work no matter what global a is in the other file 
    # I don't know how to set global environment i test file 
    # In this case it is expected that a=2

    assert prod2(2) == 40
    assert prod2(0) == 0
    assert prod2(-1) == -20


def test_longest():
    assert longest([1, 2, 3], [4, 5]) == [1, 2, 3]
    assert longest([1,2], [3,4]) == None


def test_dist():
    assert round(dist((1, 2), (3, 4)),2) == 2.83
    assert round(dist((3,4),(1,2)),2) == 2.83
    assert dist((0,0), (0,0)) == 0
