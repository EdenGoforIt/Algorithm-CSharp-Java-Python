#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
from typing import List


# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        dist = [[float("inf")] * col for _ in range(row)]
        queue = []
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            r, c = queue.pop(0)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        return dist


# @lc code=end
