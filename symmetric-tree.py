from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:

    return self.symmetrical(root, root)
  
  def symmetrical(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
    if (tree1 is None and tree2 is None): 
      return True
    if (tree1 is None or tree2 is None): 
      return False
    return (tree1.val == tree2.val) and self.symmetrical(tree1.right, tree2.left) and self.symmetrical(tree1.left, tree2.right)
    
    # return leftSymmetric == True and rightSymetric == True
    # return root.left == root.right
    
n2 = TreeNode(3)
n1 = TreeNode(2, n2)
root = TreeNode(1, None, n1)

solution = Solution()
print(solution.isSymmetric(root))