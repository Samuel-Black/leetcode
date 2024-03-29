# Definition for a binary tree node.
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
    self.count = 0

    def dfs(node):
      if node is None:
        return True

      isLeftUniValue = dfs(node.left)
      isRightUniValue = dfs(node.right)

      # If both the children form uni-value subtrees, we compare the value of
      # chidrens node with the node value.
      if isLeftUniValue and isRightUniValue:
        if node.left and node.val != node.left.val:
          return False
        if node.right and node.val != node.right.val:
          return False

        self.count += 1
        return True
      # Else if any of the child does not form a uni-value subtree, the subtree
      # rooted at node cannot be a uni-value subtree.
      return False
    
    dfs(root)
    return self.count
  
n2 = TreeNode(3)
n1 = TreeNode(2, n2)
root = TreeNode(1, None, n1)

solution = Solution()
print(solution.countUnivalSubtrees(root))