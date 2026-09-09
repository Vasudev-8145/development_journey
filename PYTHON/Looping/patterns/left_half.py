"""
*
*   *
*   *   *
*   *   *   *
"""


# print("LEFT HALF")

# def left_half():

#     for r in range(1,5):

#         for c in range(1,r+1):

#             print("*",end="\t")

#         print()

# left_half()


"""
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
"""


def left_half_num():

    for r in range(1,6):

        for c in range(1,r+1):

            print(c,end="\t")

        print()

left_half_num()