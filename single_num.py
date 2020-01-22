#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

#Note:

#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n #any num XOR'd with itself is 0, so duplicates will cancel out.
            print(result)
        return result
