class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        count = 0
        highest = 0
        d = {0:0} #Needs to be initialized from 0-0
        
        for i in range(len(nums)):
            count += nums[i] or -1
            if count not in d:
                d[count] = i+1
            else:
                highest = max(highest, i+1 - d[count])
            
        return highest
        '''
        
        #2nd Solution
        
        count = 0
        highest = 0
        d = {0:0}
        
        for i, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in d:
                highest = max(highest, i - d[count])
            else:
                d[count] = i
        return highest
            
