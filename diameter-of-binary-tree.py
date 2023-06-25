# Definition for a binary tree node.
from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
    if not root:
      return 0
    
    leftHeight = self.dfs(root.left)
    rightHeight = self.dfs(root.right)
    
    return leftHeight + rightHeight
  
  def dfs(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    leftHeight = self.dfs(root.left)
    rightHeight = self.dfs(root.right)
    return max(leftHeight, rightHeight) + 1
    
    