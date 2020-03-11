"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true
Note: You may assume both s and t have the same length.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Counting occurence of each unique character
        d = {}
        e = {}
        for i in s:
            if i not in d:
                d[i] = s.count(i)
        for j in t:
            if j not in e:
                e[j] = t.count(j)
        
        #Defining an order of each string
        order_s = []
        current = 0
        for i in range(len(s)-1):
            order_s.append(current)
            if s[i] != s[i+1]:
                current +=1
                
        new_current = 0
        order_t = []
        for k in range(len(t)-1):
            order_t.append(new_current)
            if t[k] != t[k+1]:
                new_current +=1
                
        if order_s == order_t and [d[key] for key in d] == [e[key] for key in e]:
            return True
        else: return False
        
        
            
