# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    
    
n2 = TreeNode(3)
n1 = TreeNode(2, n2)
root = TreeNode(1, None, n1)

solution = Solution()
print(solution.buildTree(root))