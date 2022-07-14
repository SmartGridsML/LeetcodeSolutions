""" Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array """

from typing import List

def maxSubArray( nums: List[int]) -> int:
        
        # Brute force
        # n = len(nums)
        # maxSum = 0
        
        # for i in range(0, len(nums)):
        #     currsum = 0 
        #     for j in range(i,  len(nums) ):
        #         currsum += nums[j]
        #         maxSum = max(maxSum , currsum)
        # return maxSum
        # KADANE ALGORITHM
        current, result = nums[0], nums[0]
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            result = max(current, result)
        return result



test = [-2, -1]

print(maxSubArray(test))
assert(maxSubArray(test) == -1)
assert(maxSubArray([5, 4, -1, 7, 8]) == 23)
