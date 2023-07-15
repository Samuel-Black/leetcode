# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def helper(inLeft: int, inRight: int) -> Optional[TreeNode]:
      if inLeft > inRight:
        return None
      
      # use the last elem in as root
      val = postorder.pop()
      root = TreeNode(val)
      
      # root splits inorder list
      # into left and right subtrees
      index = idxMap[val]
      
      # build right subtree
      root.right = helper(index + 1, inRight)
      # build left subtree
      root.left = helper(inLeft, index - 1)
      return root
    
    idxMap = {val:idx for idx, val in enumerate(inorder)} 
    return helper(0, len(inorder) - 1)

solution = Solution()
print(solution.buildTree([9,3,15,20,7], [9,15,7,20,3]))