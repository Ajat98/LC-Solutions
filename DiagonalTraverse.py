'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix
in diagonal order as shown described below.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Note: The total number of elements of the given matrix will not exceed 10,000.
'''
#Using collections defaultdict

from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        if not matrix: return out
        lines = defaultdict(list)
        
        #For a group of nums in same diagonal, sum of row + col is the same.
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(i,j)
                lines[i+j].append(matrix[i][j])
                
        for k in range(len(matrix) + len(matrix[0])-1):
            if k%2 ==0:
                out += lines[k][::-1] #reverses going across diagonal from 
            else:
                out += lines[k]
        return out
       
#Solution without imports
        if len(matrix) == 0: return []
        
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = 0
    
        out = list()
        i = 0
        while i < (m*n):
            out.append(matrix[row][col])
            if (row + col)%2 == 0:
                #upwards traversal
                if col == n-1:
                    row +=1
                elif row == 0:
                    col +=1
                else:
                    row -=1
                    col +=1
            else:
                #downwards traversal
                if row == m-1:
                    col +=1
                elif col ==0:
                    row +=1
                else:
                    row +=1
                    col -=1
                    
            i += 1
            
        return out
