# Definition for a binary tree node.
from typing import Optional
from unittest import TestCase

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def checkTree(self, root: Optional[TreeNode]) -> bool:
    
    if not root:
      return False

    def traverse(treeNode: TreeNode) -> int:
      currSum = 0
      if treeNode.left:
        # self.treeSum+=treeNode.left.val
        currSum += traverse(treeNode.left)
      if treeNode.right:
        # self.treeSum+=treeNode.right.val
        currSum += traverse(treeNode.right)
      return currSum

    res = traverse(root)
    return res == root.val

solution = Solution()
testCase = TestCase()

leaf1, leaf2 = TreeNode(4), TreeNode(6)
root1 = TreeNode(10, leaf1, leaf2)

test1 = solution.checkTree(root1)
testCase.assertTrue(test1)

leaf1, leaf2 = TreeNode(3), TreeNode(1)
root2 = TreeNode(5, leaf1, leaf2)

test2 = solution.checkTree(root2)
testCase.assertFalse(test2)