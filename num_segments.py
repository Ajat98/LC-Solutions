"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.
"""

class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        
        if not s: return 0
        for i in s.split(' '):
            if i =='' or i == ' ':
                pass
            else:
                count +=1
        return count
                
        
