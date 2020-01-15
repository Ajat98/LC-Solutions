'''
PROBLEM DESCRIPTION:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

class Solution:
    def isValid(self, s: str) -> bool:
       
        l = len(s)
        if l % 2 != 0:
            return False
        if l == 0:
            return True
        
        while "{}" in s or "()" in s or "[]" in s:
            s = s.replace('{}', '').replace('()', '').replace('[]', '')
        return s == ''
            
