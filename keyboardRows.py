# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard.
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = set('qwertyuiop')
        mid = set('asdfghjkl')
        bott = set('zxcvbnm')
        
        matches = []
        for i in words:
            w = set(i.lower())
            if (top&w == w) | (mid&w==w) | (bott&w==w):  #& is used to find intersection
                matches.append(i)
        return matches
        
                
                   
