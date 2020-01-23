#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        dict = {}
        
        for i in nums:
            if i not in dict:
                dict[i] = 1
            elif i in dict:
                dict[i] +=1
                
        for key in dict:
            if dict[key] > (len(nums) / 2):
                return key
            '''
        #Single pass dict solution
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            if d[i] > len(nums)//2:
                return i
            else:
                d[i]+=1
                
