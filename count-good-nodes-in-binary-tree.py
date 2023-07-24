# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def __init__(self):
    self.good = set()
  def goodNodes(self, root: TreeNode) -> int:
    
    if root is not None:
      if root and root.left or root and root.left and root.right
      self.goodNodes(root.left)
      self.goodNodes(root.right)

      return self.res + 1
      
    # def traverse():
      
    
solution = Solution()
print(solution.goodNodes())