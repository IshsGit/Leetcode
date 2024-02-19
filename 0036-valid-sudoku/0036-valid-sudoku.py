from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for row in board:
            if not self.is_valid(row):
                return False
        
        # Check each column
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid(column):
                return False
        
        # Check each 3x3 sub-box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid(sub_box):
                    return False
        
        return True
    
    def is_valid(self, values: List[str]) -> bool:
        seen = set()
        for val in values:
            if val != '.':
                if val in seen:
                    return False
                seen.add(val)
        return True
