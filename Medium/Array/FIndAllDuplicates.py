"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

"""
from typing import List
import collections
def findDuplicates(nums: List[int]) -> List[int]:
    counter = collections.Counter(arr)
    output = []
    for i , j in counter.items():
        if j == 2:
            output.append(i)
    return sorted(output)


arr = [4, 3, 2, 7, 8, 2, 3, 1]
out = findDuplicates(arr)
print(out)


