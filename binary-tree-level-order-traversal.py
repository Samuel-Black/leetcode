from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      res = []
      
      self.breadthFirstSearch(root, res)
      
      return res
        
    def breadthFirstSearch(self, node: Optional[TreeNode], res: List[int], level: int = 0):
      if node is None:
        return
      if node.val is not None:
        if len(res) <= level:
          res.append([])
        res[level].append(node.val)
      if node.left is not None:
        self.breadthFirstSearch(node.left, res, level + 1)
      if node.right is not None:
        self.breadthFirstSearch(node.right, res, level + 1)
      
      # add a level at the start of each recurse
      # res.append([])
      # level += 1
      
n2 = TreeNode(3)
n1 = TreeNode(2, n2)
root = TreeNode(1, None, n1)

solution = Solution()
print(solution.levelOrder(root))