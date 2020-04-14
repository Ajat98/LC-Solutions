class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        l = len(s)
        lefts = 0
        rights = 0
        for i in shift:
            if i[0] == 0:
                lefts += i[1]
            elif i[0] ==1:
                rights += i[1]
        
        if rights > lefts:
            shifted = [1, (rights - lefts)]
        elif lefts > rights:
            shifted = [0, (lefts - rights)]
        else: return s
        
        
        a = list(s)
        if shifted[0] == 1:
            for i in range(shifted[1]):
                a.insert(0, a.pop())
                
        elif shifted[0] == 0:
            for i in range(shifted[1]):
                b = a[0]
                a.append(b)
                a = a[1::]
                
                
        return ''.join([str(x) for x in a])
