"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        if 'b' and 'a' and 'l' and 'o' and 'n' in text:
            if text.count('l') >= 2 and text.count('o') >=2:
                pass
        else:
            return 0
            
        
        d = {}
        for c in text:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
                
                
        lowest = min(d['b'], d['a'], (d['l'] // 2), (d['o'] // 2), d['n'])
        return lowest
        
        
