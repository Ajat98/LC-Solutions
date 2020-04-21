# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
       
        #Initialize a counter in the top right corner, if value is zero move down, else move left
        [n,m] = binaryMatrix.dimensions()
        i = n-1
        j = m-1
        
        while i >= 0 and j >=0:
            if binaryMatrix.get(i, j) == 0:
                i -=1
            elif binaryMatrix.get(i,j) ==1:
                j -=1
        if j == m-1:
            return -1
        else:
            return j+1
        
        
