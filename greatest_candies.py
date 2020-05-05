class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''
        res, greatest  = [], max(candies)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                res.append(True)
            else:
                res.append(False)
        
        return res'''
    
    #using list comp, slightly slower
        return [ (candy + extraCandies) >= max(candies) for candy in candies ]
