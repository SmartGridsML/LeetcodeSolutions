"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List
# 2 pointer technique  - specifically - slow ; fast 


def removeDuplicates(nums: List[int]) -> int:
    #Args:
        #nums (List[int]): [description]

    #Returns:
        #int: [int ]
    

    #edge case
    if len(nums) == 0:
        return 0
    tail = 0
    for fast in range(1 , len(nums)):
        if (nums[tail] != nums[fast]):
            tail+=1
            nums[tail] = nums[fast]
    return tail + 1
    
#remove duplicates and preserve order
def removeDupes2(nums)  :
    #s = set(nums)
    return list(dict.fromkeys(nums))

ip = [1, 1, 1, 2, 2, 2, 2, 4, 5, 6, 6, 8]
ip = removeDuplicates(ip)
print(ip)

ip = removeDupes2(ip)
print("ip", ip)
