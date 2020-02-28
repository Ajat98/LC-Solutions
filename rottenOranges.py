
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        print(grid[0])
        print(grid[1])
        print(grid[2])
        rows = len(grid)
        cols = len(grid[0])
        if not rows or not cols: return 0
        
        fresh, rotten = 0, 0
        
        
        mins = 0
        bad_vals = []
        for i in range(rows):
            for c in range(cols):
                print(i, c)
                if grid[i][c] == 1:
                    fresh += 1
                if grid[i][c] == 2:
                    rotten += 1
                    bad_vals.append([i,c])
                    
        if fresh == 0: return 0
        if rotten == 0: return -1
                    
        mins = 0
        dirs = [ [-1, 0], [0,-1], [0,1], [1,0] ]
        new_rottenCount = 0
        
        while True:
            newRot = []
            for [i,j] in bad_vals:
                for d in dirs:
                    newi, newj = i+d[0], i+d[1]
                    if 0 <= newi < rows and 0 <= newj < cols and grid[newi][newj] ==1:
                        grid[newi][newj] == 2
                        newRot.append([newi, newj])
                        new_rottenCount += 1
                        
            check = newRot
            if not check:
                if new_rottenCount == fresh:
                    break
                return -1
        mins +=1
        
        return mins
