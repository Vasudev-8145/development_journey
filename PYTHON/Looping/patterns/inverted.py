"""
*   *   *   *   *
*   *   *   *   
*   *   *   
*   *   
*   

"""


# def inverted():

#     for r in range(6,1,-1):

#         for c in range(1,r):

#             print("*",end="\t")

#         print()

# inverted()


"""
1   2   3   4   5
1   2   3   4   
1   2   3   
1   2   
1   
"""


def inverted_num_column():

    for r in range(6,1,-1):

        for c in range(1,r):

            print(c,end="\t")

        print()

inverted_num_column()



