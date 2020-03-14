"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for i in strs:
            k = "".join(sorted(i))
            if k not in d:
                d[k] = [i]
            else:
                d[k] += [i]
        
        res = []
        for j in d.keys():
            res.append(d[j])
        
        return res
        
