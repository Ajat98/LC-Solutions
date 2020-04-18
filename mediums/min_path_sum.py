class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """ 
        start = grid[0][0]
        end = grid[r-1][c-1]
        unvisited =  [ [False for x in range(r)] for j in range(c)]
        distances = [ [0 for x in range(r)] for j in range(c)]
        Q = []
        tentative_dists = []
        for x in range(r):
            for j in range(c):
                v = grid[x][j]
        """
        
        r = len(grid)
        c = len(grid[0])
        
        #Stores distance from start into grid positions
        for i in range(1, c):
            grid[0][i] += grid[0][i-1]
        for i in range(1, r):
            grid[i][0] += grid[i-1][0]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min( grid[i-1][j], grid[i][j-1] )
        
        return grid[-1][-1]
                
