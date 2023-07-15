# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
from typing import List, Optional

class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def helper(inLeft: int, inRight: int) -> Optional[TreeNode]:
      nonlocal preorderIndex
      # if there are no elements to construct the tree
      if inLeft > inRight: 
        return None
      
      val = preorder[preorderIndex]
      root = TreeNode(val)


      preorderIndex += 1

      # build left and right subtree
      # excluding idxMap[root_value] element because it's the root
      root.left = helper(inLeft, idxMap[val] - 1)
      root.right = helper(idxMap[val] + 1, inRight)
      return root
      
    preorderIndex = 0
    idxMap = {val:idx for idx, val in enumerate(inorder)} 
    return helper(0, len(preorder) - 1)
  
solution = Solution()
root = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])

while root:
  print(root.val)
  root = root.left

