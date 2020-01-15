#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#Once solved, attempt to do this without converting int to a string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)
