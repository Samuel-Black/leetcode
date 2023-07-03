# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def __init__(self):
    self.subtrees = set()
    self.duplicates = []
    
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    
    leftSubtree = self.findDuplicateSubtrees(root.left)
    if leftSubtree in self.subtrees:
      self.
    rightSubtree = self.findDuplicateSubtrees(root.left)
    
    return 
    
    
    
    
solution = Solution()
print(solution.findDuplicateSubtrees())