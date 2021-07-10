email = 'jeffreywei@berkeley.edu'

def currency(cookie, drawer):
    """
    Write a function `currency` that takes in two lists.
        `cookie` is a list of strings
        `drawer` is a list of integers

    It returns a new list where every element from `cookie` is copied the
    number of times as the corresponding element in `drawer`. If the number
    of times to be copied is negative (-k), then it removes the previous
    k elements added.

    Note 1: `cookie` and `drawer` do not have to be the same length, simply ignore
    any extra elements in the longer list.

    Note 2: you can assume that you will never be asked to delete more
    elements than exist


    >>> currency(['a', 'b', 'c'], [1, 2, 3])
    ['a', 'b', 'b', 'c', 'c', 'c']
    >>> currency(['a', 'b', 'c'], [3])
    ['a', 'a', 'a']
    >>> currency(['a', 'b', 'c'], [0, 2, 0])
    ['b', 'b']
    >>> currency([], [1,2,3])
    []
    >>> currency(['a', 'b', 'c'], [1, -1, 3])
    ['c', 'c', 'c']
    """
    # def currency_helper(c, d, r):
    #     if len(c) == 0 or len(d) == 0:
    #         return r
    #     if d[0] > 0:
    #         r = r + d[0] * [c[0]]
    #     else:
    #         r = r[:len(r) + d[0]]
    #     return currency_helper(c[1:], d[1:], r)
    # return currency_helper(cookie, drawer, [])

    def copycat_helper(lst1, lst2, lst_so_far):
        if len(lst1) == 0 or len(lst2) == 0:
            return lst_so_far
        if lst2[0] >= 0:
            lst_so_far = lst_so_far + [lst1[0] for _ in range(lst2[0])]
        else:
            print(lst_so_far)
            lst_so_far = lst_so_far[:lst2[0]]
        return copycat_helper(lst1[1:], lst2[1:], lst_so_far)
    return copycat_helper(cookie, drawer, [])

if __name__ == "__main__":
    print(currency(['a', 'b', 'c'], [1, 2, 0]))

# ORIGINAL SKELETON FOLLOWS

# def currency(cookie, drawer):
#     """
#     Write a function `currency` that takes in two lists.
#         `cookie` is a list of strings
#         `drawer` is a list of integers

#     It returns a new list where every element from `cookie` is copied the
#     number of times as the corresponding element in `drawer`. If the number
#     of times to be copied is negative (-k), then it removes the previous
#     k elements added.

#     Note 1: `cookie` and `drawer` do not have to be the same length, simply ignore
#     any extra elements in the longer list.

#     Note 2: you can assume that you will never be asked to delete more
#     elements than exist


#     >>> currency(['a', 'b', 'c'], [1, 2, 3])
#     ['a', 'b', 'b', 'c', 'c', 'c']
#     >>> currency(['a', 'b', 'c'], [3])
#     ['a', 'a', 'a']
#     >>> currency(['a', 'b', 'c'], [0, 2, 0])
#     ['b', 'b']
#     >>> currency([], [1,2,3])
#     []
#     >>> currency(['a', 'b', 'c'], [1, -1, 3])
#     ['c', 'c', 'c']
#     """
#     def currency_helper(______, ______, ______):
#         if ______:
#             return ______
#         if ______:
#             ______ = ______
#         else:
#             ______ = ______[:______]
#         return ______
#     return ______
