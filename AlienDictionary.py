class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #give index of particular chars in the Alien Dict
        words_values = [[order.index(char) for char in list(word)] for word in words]
        
        while len(words_values) > 1:
            #compare 1st word to 2nd and if it's before, remove it from list. When 1 word left, all words are in order
            
            for i in range(len(words_values[0])):
                if words_values[0][i] > words_values[1][i]:
                    return False
                elif words_values[0][i] < words_values[1][i]:
                    words_values = words_values[1:]
                    break
                
                if i == len(words_values[0]) -1:
                    words_values = words_values[1:]
                elif i == len(words_values[1]) - 1:
                    return False
                
        return True
