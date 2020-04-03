class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_arr1 = nums[0]
        res = sub_arr1
        
        
        for i in range(1, (len(nums))):
            #If previous subarray + current position is greater than previous subarray, current pos is added on.
            if sub_arr1 + nums[i] >= nums[i]:
                sub_arr1 += nums[i]
            #If position is greater than current subarr, replace entire subarr with current position
            elif sub_arr1 + nums[i] < nums[i]:
                sub_arr1 = nums[i]
            #if subarray greater than res, update res to current subarr
            if sub_arr1 > res:
                res = sub_arr1
        
        return res
