# Definition for a binary tree node.
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None: 
      return 0 
    else: 
      left_height = self.minDepth(root.left) 
      right_height = self.minDepth(root.right) 
      if left_height == 0:
        return right_height + 1
      elif right_height == 0:
        return left_height + 1
      else:
        return min(left_height, right_height) + 1 
      
    
    
solution = Solution()
print(solution.minDepth())