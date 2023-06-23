from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    self.printTree(root, res)
      
    return res
  
  def printTree(self, node: Optional[TreeNode], res: List[int]) -> None:
    if node is None:
      return
    if node.val is not None:
      res.append(node.val)
    if node.left is not None:
      self.printTree(node.left, res)
    if node.right is not None:
      self.printTree(node.right, res)

n2 = TreeNode(3)
n1 = TreeNode(2, n2)
root = TreeNode(1, None, n1)

solution = Solution()
print(solution.preorderTraversal(root))