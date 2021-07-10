email = 'jeffreywei@berkeley.edu'

def carat(puma, k):
    """
    Given a number `puma`, finds the largest number of length `k` or fewer,
    composed of digits from `puma`, in order.

    >>> carat(1234, 1)
    4
    >>> carat(32749, 2)
    79
    >>> carat(1917, 2)
    97
    >>> carat(32749, 18)
    32749
    """
    if puma == 0 or k == 0:
        return 0
    a = carat(puma // 10, k - 1) * 10 + puma % 10
    b = carat(puma // 10, k)
    return max(a, b)

# ORIGINAL SKELETON FOLLOWS

# def carat(puma, k):
#     """
#     Given a number `puma`, finds the largest number of length `k` or fewer,
#     composed of digits from `puma`, in order.

#     >>> carat(1234, 1)
#     4
#     >>> carat(32749, 2)
#     79
#     >>> carat(1917, 2)
#     97
#     >>> carat(32749, 18)
#     32749
#     """
#     if ______:
#         return ______
#     a = ______
#     b = ______
#     return ______
