"""Exercises with simple functions"""


from math import sqrt
from re import A


def prod(a, b, c):
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    6

    >>> prod(0, 1, 2)
    0

    >>> prod(1, -2, 5)
    -10
    """

    result = a*b*c
    return result
    ...
a=2

def prod2(b):
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> a = 2
    >>> prod2(42)
    840
    
    """

    c = 10
    result = prod(a, b, c)
    return result
    ...


def longest(x, y):
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    [1, 2, 3]

    >>> longest([1,2], [3,4])
    
    """
    if len(x)==len(y):
        return None 
    elif len(x) > len(y):
        longest = x
    else: 
        longest = y
    return longest
    ...


def dist(p1, p2):
    """
    Compute the distance between p1 and p2.

    >>> round(dist((1,2), (3,4)),2)
    2.83

    >>> round(dist((3,4),(1,2)),2)
    2.83

    >>> dist((0,0),(0,0))
    0.0

    """
    x1, y1 = p1
    x2, y2 = p2

    from math import sqrt
    from math import isclose
    result = sqrt((x1-x2)**2 + (y1-y2)**2)

    return result
    ...
