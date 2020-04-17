class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        #initialize False values for all coordinates not yet visited
        visited = [ [False for i in range(cols)] for i in range(rows)]
        
        #sets coordinate vals to True if we have visited them as part of an island
        def DFS(i, k):
            if i < 0 or i >= rows or k < 0 or k >= cols or grid[i][k] == '0' or visited[i][k]:
                return
            visited[i][k] = True
            #Checking top, bottom, right, left directions of current coordinate.
            DFS(i + 1, k)
            DFS(i -1, k)
            DFS(i, k +1)
            DFS(i, k-1)
            
        
        count = 0
        for i in range(rows):
            for k in range(cols):
                #If a coord has not been visited by another search and is not 0, it would be a new island
                if not visited[i][k] and grid[i][k] == '1':
                    DFS(i, k)
                    count += 1
                    
        return count
                        
                        
