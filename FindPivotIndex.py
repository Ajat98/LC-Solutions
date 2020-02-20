"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return -1
        
        for x, i in enumerate(nums):
            lista = nums[:x]
            listb = nums[x+1::]
            if sum(lista) == sum(listb):
                return x
            print(x,i)
            if x == (len(nums)-1):
                return -1
        
