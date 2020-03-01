"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
""" 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        d = {}
        
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
            
        check = False    
        for k in d:
            if d[k] >= 2:
                check = True
                
        return check
        '''
        
    #One liner solution
        return len(nums) != len(set(nums))
