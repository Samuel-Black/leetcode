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
    
  def dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return
    if root.left:
      leftSubtree = self.dfs(root.left)
      if leftSubtree and leftSubtree.val in self.subtrees:
        self.duplicates.append(leftSubtree.val)
      if leftSubtree and leftSubtree.val: 
        self.subtrees.add(leftSubtree)
    if root.right:
      rightSubtree = self.dfs(root.left)
      if rightSubtree and rightSubtree.val in self.subtrees:
        self.duplicates.append(rightSubtree.val)
      if rightSubtree and rightSubtree.val: 
        self.subtrees.add(rightSubtree)
    
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    res = self.dfs(root)
    print(res)
    
    
leafLeft3 = TreeNode(5)
leafLeft2 = TreeNode(4)
leafLeft1 = TreeNode(2, leafLeft2, leafLeft3)

leafRight3 = TreeNode(7)
leafRight2 = TreeNode(6)
leafRight1 = TreeNode(3, leafRight2, leafRight3)

root = TreeNode(1, leafLeft1, leafRight1)
solution = Solution()
print(solution.findDuplicateSubtrees(root))