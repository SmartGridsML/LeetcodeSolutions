from typing import List
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
#
# RUNTIME: 28 ms, MEMORY faster than 84.79%


def generate(numRows: int) -> List[List[int]]:
    pascalTriangle = [[1]]
    print(pascalTriangle[0])
    for line in range(2, numRows+1):
        newline = [1]
        for i in range(1, line-1):  # line-1 as we already have base case
            # next value is sum of element above AND above left
            newline.append(pascalTriangle[-1][i-1] + pascalTriangle[-1][i])
        newline.append(1)
        pascalTriangle.append(newline)
        print(newline)
    return pascalTriangle


def memoizedRec(numRows: int) -> List[List[int]]:
    # generate a new array
    res = [[0 for _ in range(i+1)] for i in range(numRows)]

    def helper(i, j):
        # base case
        if j == 0 or j == i:
            return 1
        if res[i][j] == 0:
            res[i][j] = helper(i-1, j-1) + helper(i-1, j)
        return res[i][j]

    for i in range(numRows):
        row = res[i]
        for j in range(i+1):
            row[j] = helper(i, j)

    return res


ls = [[]]
ls = generate(3)
print (ls)


ls_m = [[]]
ls_m = generate(3)
print (ls_m)