"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = {}
        for i in s:
            if i in d:
                d[i]+= 1
            else:
                d[i] = 1
        
        check = False
        for k in d.keys():
            if d[k] == 1:
                return s.index(k)
                check = True
                break
        if check == False:
            return -1
