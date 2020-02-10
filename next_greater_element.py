#You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
#Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

#The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
#If it does not exist, output -1 for this number.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        
        for i, n1 in enumerate(nums2):
            print(i, n1)
            for n2 in nums2[i+1:]:
                if n1 < n2:
                    d[n1] = n2
                    break
        return [d.get(num1, -1) for num1 in nums1] #tries to get num1 from dict, if val not found returns -1
