class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        #return address.replace('.', '[.]')
    
        #Or (slightly faster)
        #return '[.]'.join(address.split('.'))
        
        #OR
        res = []
        for c in address:
            if c != '.':
                res.append(c)
            else:
                res.append('[.]')
        return "".join(res)
