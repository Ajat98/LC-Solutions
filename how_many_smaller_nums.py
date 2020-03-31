class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        results = []
        
        ordered = sorted(nums)
        count = 0
        for i in range(len(nums)):
            for k in ordered:
                if k < nums[i]:
                    count += 1
            results.append(count)
            count = 0
        return results
        """
        #Alternate Solution using hashmap (faster)
    
        newNums = sorted(nums)
        c = {}
        
        #index of num shows number of nums that are before it
        for i in range(len(newNums)):
            if newNums[i] not in c:
                c[newNums[i]] = i
        
        # change nums[i] to value of nums[i] from previous dict
        for i in range(len(nums)):
            nums[i] = c[nums[i]]
    
        return nums
                
