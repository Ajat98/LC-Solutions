"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 3
Output: [1,3,3,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        p = [[1] * (i+1) for i in range(rowIndex+1)] #generate triange + rows of all 1s
        
        for i in range(1, rowIndex+1):
            for k in range(1, i):
                p[i][k] = p[i-1][k-1] + p[i-1][k] 
        return p[rowIndex]
        
