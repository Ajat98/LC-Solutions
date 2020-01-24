#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it.
'''Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #if numRows == 0:
           # return []
        
        #initialize LoL with 1s as placeholders
        p = [[1] * (i+1) for i in range(numRows)]
        print(p)
        
        for i in range(numRows):
            for k in range(1, i):
                p[i][k] = p[i-1][k-1] + p[i-1][k]
        return p
            
