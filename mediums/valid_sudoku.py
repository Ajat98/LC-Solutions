"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Initialize dictionaries for columns and 3x3 squares, 
        
        columns = [{} for i in range(9)]
        quadrants = [ [{} for i in range(3)] for k in range(3)]
        
        for i in range(9):
            row = {} #resets
            for j in range(9):
                column = columns[j]
                threeByThree = quadrants[i // 3][j // 3]
                num = board[i][j]
                
                #ignoring empty spaces, checks if num is already in current row, column, or 3x3.
                if num != "." and (num in row or num in column or num in threeByThree):
                    return False
                else:
                    row[num] = 1
                    column[num] = 1
                    threeByThree[num] = 1          
        return True
                
                
       
        
