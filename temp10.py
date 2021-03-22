
def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> lst = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst, 2)
    9
    >>> lst2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    # Here?
    count = 1
    current = None
    prev = None
    while True:
        current = t.__next__()
        if current == prev:
            count += 1
        else:
            prev = current
            count = 1
        if count == k:
            #if count matches then we print the value and come out of the loop
            #break is easy to understand
            print(current)
            break


lst = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
repeated(lst, 2)
lst2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
repeated(lst2, 3)
s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
repeated(s, 3)
repeated(s, 3)
s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
repeated(s2, 3)