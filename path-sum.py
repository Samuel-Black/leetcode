# Definition for a binary tree node.
from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
    if root is None:
      return False
    
    targetSum -= root.val
    
    if root.right is None and root.left is None:
      return targetSum == 0
    
    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
n2 = TreeNode(3)
n1 = TreeNode(2, n2)
root = TreeNode(1, None, n1)

solution = Solution()
print(solution.hasPathSum(root, 5))
