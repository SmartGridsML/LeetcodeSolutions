# Given an integer array nums of 2n integers, group these integers into n pairs 
# (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. 
# Return the maximized sum.

from typing import List
import itertools

def maxRow(nums: List[int]) -> int:
    m = len(nums)
    n = len(nums[0])
    

def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    i , j = 0 , len(nums)-1
    pairs = []
    mins = []
    while(i < j):
        pairs.append([nums[i] , nums[j]])
        i+=1
        j-=1
    for row in pairs:
        mins.append(min(row))
    return sum(mins)

nums = [1,4,3,2 , 5, 6] 
result = arrayPairSum(nums)
print (result)
''' pairGen = [(x, y) for x in nums for y in nums if y > x]
pairw = list(itertools.combinations(nums, 2))
for i in pairGen:
    print(i)
print(pairw) '''