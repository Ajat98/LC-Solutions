class Solution:
    def checkValidString(self, s: str) -> bool:
        
        s1 = []
        #Left to right, test for (, knowing * can balance all the )
        for i in s:
            if i =='(' or i =='*':
                s1.append(i)
            else:
                if len(s1) > 0:
                    s1.pop()
                else:
                    return False #Because there is not enough ( left
                
        
    
        s2 = []
        #testing all ) and * will balance the (
        #right to left
        for i in s[::-1]:
            if i == ')' or i =='*':
                s2.append(i)
            else:
                if len(s2) > 0:
                    s2.pop()
                else: 
                    return False
                    #Becasue there are not enough )
                    
        return True
