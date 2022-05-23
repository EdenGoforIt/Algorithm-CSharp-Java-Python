#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#


# @lc code=start
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        if not board or len(board) == 0:
            return
        self.solve(board)

    def solve(self, board) -> bool:

        for r in range(len(board)):  # rows
            for c in range(len(board[0])):  # column
                if board[r][c] == ".":  # we need to find the right number
                    for v in "123456789":  # v for values from 1 to 9
                        if self.isValid(board, r, c, v):
                            board[r][c] = v
                            if self.solve(board):
                                return True
                            else:
                                board[r][c] = "."
                    
                    # if not 
                    return False
        
        return True

    def isValid(self, board, r, c, v) -> bool:
        for i in range(9):
            if board[r][i] == v:  # if row has the Value already then not a good number
                return False
        for j in range(9):
            if board[j][c] == v:
                return False

        for i in range(3):
            for j in range(3):
                if board[(r//3)*3 + i][(c//3)*3 + j] == v:
                    return False
        
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(Solution().solveSudoku(board))
# @lc code=end
