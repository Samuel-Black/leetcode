from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    return self.dfs(root)[0]
  
  def dfs(self, root: Optional[TreeNode]) -> tuple([bool, int]):
    if not root:
      return True, -1
    left_balanced, left_height = self.dfs(root.left)
    right_balanced, right_height = self.dfs(root.right)

    if left_balanced == False or right_balanced == False:
        return False, 0
    # if left_height == 0 and right_height >= 1:
    #   return -1
    # else:
    return (abs(left_height - right_height) < 2), 1 + max(left_height, right_height)
    
    