# Return the minimum number of operations needed to make nums strictly increasing.
from typing import List

def minOperations(nums: List[int]) -> int: 
    if len(nums) == 1:
            return 0
    minO = 0
    for i in range(1 , len(nums)):
        # conditional provides minor optimisation
        if nums[i] <= nums[i-1]:
            temp = nums[i]
            nums[i] = max(nums[i-1] + 1, nums[i])
            minO += (nums[i] - temp)
            
    return minO
