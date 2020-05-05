class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        '''
        jewels = [x for x in J]
        count = 0
        for c in S:
            if c in jewels:
                count +=1
        return count
        '''
    #One Liner
        return sum([s in J for s in S])
