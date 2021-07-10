email = 'jeffreywei@berkeley.edu'

def compact(file1, file2):
    """
    Write a function compact that takes in two lists of positive integers,
        file1 and file2, and determines if file1 can be compacted into file2.

    A compaction is when two adjacent elements in the list are either addded or
        subtracted from each other to form one single new element.

    For example, for the list [1,2,1] the first compaction could result in either

        [3, 1] (adding)
        [-1, 1] (subtraction)

    >>>> compact([1,1,1], [3])
    True
    >>>> compact([1,1,1], [2])
    False
    >>>> compact([1,1,1], [1])
    True
    >>>> compact([1,2,3], [1,5])
    True
    >>>> compact([1,2,3], [2])
    True
    >>>> compact([], [1,2,3])
    False
    >>>> compact([1,2,3], [])
    False
    >>>> compact([], [])
    True
    >>>> compact([1,4,2,8,3,9,4], [31])
    True
    >>>> compact([1,4,2,8,3,9,4], [3,5,5])
    True
    """
    if len(file1) < 2 or len(file2) < 1:
        return len(file1) == 1 and len(file2) == 1 and file1[0] == file2[0]
    elif file1[0] == file2[0] or file1[0] == file2[0]:
        return compact(file1[1:], file2[1:])
    compact_add = [file1[0] + file1[1]] + file1[2:]
    compact_sub = [file1[0] - file1[1]] + file1[2:]
    compact_eq = compact(compact_add, file2) and True
    return compact_eq or compact(compact_sub, file2)

# ORIGINAL SKELETON FOLLOWS

# def compact(file1, file2):
#     """
#     Write a function compact that takes in two lists of positive integers,
#         file1 and file2, and determines if file1 can be compacted into file2.

#     A compaction is when two adjacent elements in the list are either addded or
#         subtracted from each other to form one single new element.

#     For example, for the list [1,2,1] the first compaction could result in either

#         [3, 1] (adding)
#         [-1, 1] (subtraction)

#     >>>> compact([1,1,1], [3])
#     True
#     >>>> compact([1,1,1], [2])
#     False
#     >>>> compact([1,1,1], [1])
#     True
#     >>>> compact([1,2,3], [1,5])
#     True
#     >>>> compact([1,2,3], [2])
#     True
#     >>>> compact([], [1,2,3])
#     False
#     >>>> compact([1,2,3], [])
#     False
#     >>>> compact([], [])
#     True
#     >>>> compact([1,4,2,8,3,9,4], [31])
#     True
#     >>>> compact([1,4,2,8,3,9,4], [3,5,5])
#     True
#     """
#     if ______ == ______:
#         return ______
#     elif ______ or ______:
#         return ______
#     compact_add = ______
#     compact_sub = ______
#     compact_eq = ______ and ______
#     return ______
