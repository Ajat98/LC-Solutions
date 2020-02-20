"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.
"""
#Messy Solution

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        dominant = max(nums)
        place = nums.index(dominant)
        nums[place] = 0
        dominantCheck = True
        
        for i in nums:
            if  i*2 > dominant:
                dominantCheck = False
        if dominantCheck == False: 
            return -1
        else:
            return place
        
