"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a, b):
    
    """
    type a: str
    type b: str
    rtype: str
    """
    
        a = a[::-1]
        b = b[::-1]
        
        if len(a) < len(b):
            for i in range(len(a), len(b)):
                a+= '0'
        elif len(a) > len(b):
            for i in range(len(b), len(a)):
                b+= '0'
        
        n = len(a)
        carry = 0
        s = ''
        
        for i in range(n):
            l,m,c = int(a[i]), int(b[i]), carry
            s += str(l^m^c) #sum is XOR of three bits
            carry = (l&m) | (m&c) | (c&l) #carry is pairwise and of three bits
            
        if carry==1:
            s+= str(carry)
        return s[::-1]
