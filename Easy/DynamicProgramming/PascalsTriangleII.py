# Runtime: 32 ms, faster than 65.71 % of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 13.9 MB,


from typing import List


def getRow(rowIndex: int) -> List[int]:
      pascalsTriangle = [[1]]
      for line in range(2, rowIndex+2):
           newline = [1]
           for i in range(1, line - 1):
                newline.append(pascalsTriangle[-1]
                               [i-1] + pascalsTriangle[-1][i])
           newline.append(1)
           pascalsTriangle.append(newline)
      # returns last row of 2d mtrix
      return pascalsTriangle[-1]
