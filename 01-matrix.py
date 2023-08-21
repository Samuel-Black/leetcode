from typing import List
import unittest

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        matrix = [row[:] for row in mat]
        m = len(matrix)
        n = len(matrix[0])
        queue = deque()
        seen = set()
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))
                    seen.add((row, col))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, steps = queue.popleft()
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    matrix[next_row][next_col] = steps + 1
        
        return matrix

# class Solution:
#   def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    
#     n = len(mat)
#     m = len(mat[0])
    
#     directions = [
#       [-1, 0], # up
#       [1, 0], # down
#       [0, -1], # left
#       [0, 1], # right
#     ]
    
#     visited = set()
    
#     for i in range(0, n):
#       for j in range(0, m):
#         if mat[i][j] == 1:
#           minDistance = (10**8)+1
#           for direction in directions:
#             row = i + direction[0]
#             col = j + direction[1]
#             if col >= 0 and col < m and row >= 0 and row < n:
#               minDistance = min(minDistance, mat[row][col])
#           mat[i][j] = minDistance + 1
#         visited.add()
#     return mat
    
solution = Solution()
test = unittest.TestCase()
# test1 = solution.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
# test.assertEqual(test1, [[0,0,0],[0,1,0],[0,0,0]])
# test2 = solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
# test.assertEqual(test2, [[0,0,0],[0,1,0],[1,2,1]])
# test3 = solution.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
# test.assertEqual(test3, [[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
test4 = solution.updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]])
test.assertEqual(test4, [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]])
