# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None: 
      return 0 
    else: 
      left_height = self.maxDepth(root.left) 
      right_height = self.maxDepth(root.right) 
      return max(left_height, right_height) + 1 
      
n2 = TreeNode(3)
n1 = TreeNode(2, n2)
root = TreeNode(1, None, n1)

solution = Solution()
print(solution.maxDepth(root))