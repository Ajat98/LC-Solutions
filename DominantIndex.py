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
        
 #Another simple Solution, O(n) time and O(1) space.
 #compare the largest number with 2x the second largest number.
	    max1 = 0
        max2 = 0
        
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
                
        if max1 >= max2*2:
            return nums.index(max1)
        else:
            return -1
