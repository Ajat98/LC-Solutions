'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Assume all given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #for empty list
        if not strs: 
            return "" 
        
        #shortest str in list will be used as largest possible prefix
        smallest = min(strs, key=len)

        for i, char in enumerate(smallest):
            for c in strs:
                if c[i] != char:
                    return smallest[:i]
        return smallest
                       
