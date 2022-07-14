"""
Given an array of integers nums and an integer target,
 return indices of the two numbers such that they add up to target.
 You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement not in seen:
                seen[num] = index
            else:
                return sorted([index, seen[complement]])
        return None
    
nums = [2,7,11,15]
target = 26
print(twoSum(nums, target))
