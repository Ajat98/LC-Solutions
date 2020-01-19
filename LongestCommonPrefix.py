'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Assume all given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ''
            
        #upper bound of longest common prefix will shortest string in strs
        smallest = min(strs, key=len) 
        
        for i, char in enumerate(smallest): 
            #Upper bound of
            for k in strs:
                if k[i] != char:
                    return smallest[:i]
        return smallest
            
                       
