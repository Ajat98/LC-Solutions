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
        for word in strs:
            k = "".join(sorted(word))
            
            #Word must be inserted as a list
            if k not in d:
                d[k] = [word]
            else:
                d[k] += [word]
        
        res = []
        for j in d.keys():
            res.append(d[j])
        return res
        
