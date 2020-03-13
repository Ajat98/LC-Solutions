"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        
        for i in nums1:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        
        z = {}
        for j in nums2:
            if j not in d:
                d[j] = 1
            else:
                d[j] +=1
        
        results = []
        
        for k in d.keys():
            if k in nums2:
                for i in range(min(nums1.count(k), nums2.count(k))):
                    results.append(k)
        return results
        
