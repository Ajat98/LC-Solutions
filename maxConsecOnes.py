"""
Given a binary array, find the maximum number of consecutive 1s in this array.
Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#First draft solution (messy)
        k = 1
        check = []
        if len(nums) == 1:
            if nums[0] == 1: return 1
            else: return 0
            
        if 1 not in nums:
            return 0
        
        for i in range(len(nums)-1):
            if nums[i] ==1:
                if nums[i+1] == 1:
                    k+=1
                check.append(k)
            elif nums[i] != 1:
                k = 1
                check.append(k)
        return max(check)
        
#2nd Solution
        c = 0
        mx = 0
        for i in nums:
            if i ==1:
                c +=1
            if c > mx:
                mx = c
            if i == 0:
                c = 0
        return mx
