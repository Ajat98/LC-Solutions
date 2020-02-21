"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        
        out = list()
        m = len(matrix)
        n = len(matrix[0])
       
        
        left = 0
        right = n-1
        top = 0
        bottom = m-1
        
        while left <= right and top <= bottom:
            #moving left
            for i in range(left, right +1):
                out.append(matrix[left][i])
            top+=1
            
            #move down
            for i in range(top, bottom +1):
                out.append(matrix[i][right])
            right -=1
            
            if top<= bottom:
                #move left
                for i in range(right, left-1, -1):
                    out.append(matrix[bottom][i])
                bottom -=1
            
            if left <= right:
                #move up
                for i in range(bottom, top-1, -1):
                    out.append(matrix[i][left])
                left +=1
                 
            
        return out
