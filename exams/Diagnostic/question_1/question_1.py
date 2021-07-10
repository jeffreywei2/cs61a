email = 'jeffreywei@berkeley.edu'

def skyscraper(thorium, fn_even, fn_odd):
    """
    Write a function `skyscraper` that takes in a positive integer `thorium` and two
    functions `fn_even` and `fn_odd`.

    It applies `fn_even` to all of the even digits in the integer and
    applies `fn_odd` to all of the odd digits in the integer. It then returns whether
    the result of the even values is greater than the result of the odd values.
    You can guarantee that the number has at least one even and odd digit.

    >>> skyscraper(1234, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 > 3 * 1
    True
    >>> skyscraper(11111111111112, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1 * 1 * ... * 1
    True
    >>> skyscraper(11111111111112, lambda x,y: x+y, lambda x,y: x+y) # 2 <= 1 + 1 + ... + 1
    False
    >>> skyscraper(12, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1
    True
    >>> skyscraper(12345, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 <= 1 * 3 * 5
    False
    >>> skyscraper(18383, lambda x,y: x-y, lambda x,y: x-y) # 8 - 8 > 3 - 3 - 1
    True
    """
    evens_defined, odds_defined = False, False
    evens, odds = None, None
    while thorium > 0:
        thorium, last = thorium // 10, thorium % 10
        if last % 2 == 0:
            if evens_defined == True:
                evens = fn_even(evens, last)
            else:
                evens_defined, evens = True, last
        else:
            if odds_defined == True:
                odds = fn_odd(odds, last)
            else:
                odds_defined, odds = True, last
    return evens > odds

# ORIGINAL SKELETON FOLLOWS

# def skyscraper(thorium, fn_even, fn_odd):
#     """
#     Write a function `skyscraper` that takes in a positive integer `thorium` and two
#     functions `fn_even` and `fn_odd`.

#     It applies `fn_even` to all of the even digits in the integer and
#     applies `fn_odd` to all of the odd digits in the integer. It then returns whether
#     the result of the even values is greater than the result of the odd values.
#     You can guarantee that the number has at least one even and odd digit.

#     >>> skyscraper(1234, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 > 3 * 1
#     True
#     >>> skyscraper(11111111111112, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1 * 1 * ... * 1
#     True
#     >>> skyscraper(11111111111112, lambda x,y: x+y, lambda x,y: x+y) # 2 <= 1 + 1 + ... + 1
#     False
#     >>> skyscraper(12, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1
#     True
#     >>> skyscraper(12345, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 <= 1 * 3 * 5
#     False
#     >>> skyscraper(18383, lambda x,y: x-y, lambda x,y: x-y) # 8 - 8 > 3 - 3 - 1
#     True
#     """
#     evens_defined, odds_defined = False, False
#     evens, odds = None, None
#     while ______:
#         ______ = ______
#         if ______:
#             if ______:
#                 ______
#                 ______
#             else:
#                 ______
#         else:
#             if ______:
#                 ______
#                 ______
#             else:
#                 ______
#     return evens > odds
