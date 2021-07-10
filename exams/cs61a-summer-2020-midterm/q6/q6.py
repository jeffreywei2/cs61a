email = 'jeffreywei@berkeley.edu'

def subpizza(tale):
    """
    A 'pizza' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
        1
        4444
        7777777

    Note that `1 <= d <= 9`; there are no 0-length pizzas.

    Your task is to implement the `subpizza` function, which takes in an integer `tale` and returns
        whether `tale` contains a pizza as a consecutive subinteger of its digits.

    >>> subpizza(2233) # 22 counts
    True
    >>> subpizza(2444423) # 4444 counts
    True
    >>> subpizza(82223) # 22 counts even if it appears as part of 222
    True
    >>> subpizza(234562) # 2...2 does not count if the 2s are not consecutive
    False
    >>> subpizza(1) # 1 counts
    True
    >>> subpizza(498729879871) # 1 counts
    True
    >>> subpizza(149872987987) # 1 counts
    True
    >>> subpizza(4445555) # no pizzas in this number
    False
    >>> subpizza(20) # no pizzas in this number
    False
    """
    current_digit = tale % 10
    count = 0
    while tale > 0:
        last = current_digit
        if tale % 10 == last:
            count += 1
        else:
            count = 1
            current_digit = tale % 10
        if count == last:
            return True
        tale = tale // 10
    return count == current_digit

# ORIGINAL SKELETON FOLLOWS

# def subpizza(tale):
#     """
#     A 'pizza' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
#         1
#         4444
#         7777777

#     Note that `1 <= d <= 9`; there are no 0-length pizzas.

#     Your task is to implement the `subpizza` function, which takes in an integer `tale` and returns
#         whether `tale` contains a pizza as a consecutive subinteger of its digits.

#     >>> subpizza(2233) # 22 counts
#     True
#     >>> subpizza(2444423) # 4444 counts
#     True
#     >>> subpizza(82223) # 22 counts even if it appears as part of 222
#     True
#     >>> subpizza(234562) # 2...2 does not count if the 2s are not consecutive
#     False
#     >>> subpizza(1) # 1 counts
#     True
#     >>> subpizza(498729879871) # 1 counts
#     True
#     >>> subpizza(149872987987) # 1 counts
#     True
#     >>> subpizza(4445555) # no pizzas in this number
#     False
#     >>> subpizza(20) # no pizzas in this number
#     False
#     """
#     current_digit = ______
#     count = ______
#     while ______:
#         last = ______
#         if ______:
#             count += 1
#         else:
#             count = ______
#             ______
#         if ______:
#             ______
#         tale = ______
#     return ______
