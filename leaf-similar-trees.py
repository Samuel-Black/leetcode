# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    
    def traverse(root: Optional[TreeNode], arr: List[int]):
      if root and not root.left and not root.right:
        arr.append(root.val)
        return
      else:
        if root and root.left:
          traverse(root.left, arr)
        if root and root.right:
          traverse(root.right, arr)
        
    leaf1 = []
    leaf2 = []
    traverse(root1, leaf1)
    traverse(root2, leaf2)
    
    return leaf1 == leaf2
        
    
    

solution = Solution()
print(solution.leafSimilar())