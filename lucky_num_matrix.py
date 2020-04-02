class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix[0])
        cols = len(matrix)
        
        potential = []
        results = []
        
        #finds smallest nums in each row.
        for i in range(cols):
            potential.append(min(matrix[i]))
        
        
        for k in range(rows):
            maxCol = matrix[0][k]
            
            for j in range(cols):
                if matrix[j][k] > maxCol:
                    maxCol = matrix[j][k]
            
            if maxCol in potential:
                results.append(maxCol)
        
        return results
