from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      res = []
      
      self.treeTraversal(root, res)
      
      return res
    
    def treeTraversal(self, node: Optional[TreeNode], res: List[int]) -> None:
      if node is None:
        return
      if node.left is not None:
        self.treeTraversal(node.left, res)
      if node.right is not None:
        self.treeTraversal(node.right, res)
      if node.val is not None:
        res.append(node.val)

n2 = TreeNode(3)
n1 = TreeNode(2, n2)
root = TreeNode(1, None, n1)

solution = Solution()
print(solution.postorderTraversal(root))