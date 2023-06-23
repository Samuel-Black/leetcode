# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    
    if root is None:
      return res
    
    if root.left is not None:
      self.traverseTree(root.left, res)
    if root.val is not None:
      res.append(root.val)
    if root.right is not None:
      self.traverseTree(root.right, res)
    
    return res
  
  def traverseTree(self, node: Optional[TreeNode], res: List[int]) -> None:
    if node is None:
      return
    if node.left is not None:
      self.traverseTree(node.left, res)
    if node.val is not None:
      res.append(node.val)
    if node.right is not None:
      self.traverseTree(node.right, res)
    
      
n2 = TreeNode(3)
n1 = TreeNode(2, n2)
root = TreeNode(1, None, n1)

solution = Solution()
print(solution.inorderTraversal(root))