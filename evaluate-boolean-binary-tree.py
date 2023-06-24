# Definition for a binary tree node.
from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def evaluateTree(self, root: Optional[TreeNode]) -> bool:
    # 0 == True
    # 1 == False
    # 2 == or
    # 3 == and
    res = False
    if root.val == 2:
      res = self.evaluateTree(root.left) or self.evaluateTree(root.right)
    elif root.val == 3:
      res = self.evaluateTree(root.left) and self.evaluateTree(root.right)
    else:
      res = bool(root.val)
    
    return res