#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#Once solved, attempt to do this without converting int to a string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #return str(x)[::-1] == str(x) #Using str()

#WITHOUT USING STR()
        if x < 0: #any negative num will not be palindrome
           return False 
        
        a, rem = x, 0
        while a: #while a !=0
            rem = rem * 10 + a % 10
            a = int(a/10)
        return rem == x
    
