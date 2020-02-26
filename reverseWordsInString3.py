"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        
        x = s.split(' ')
        print(x)
        
        val = ''
        
        c = 0 
        for i in x:
            r = i[::-1]
            print(r)
            val += r
            if c < len(x) -1:
                val += " "
                c += 1
        return val
        
