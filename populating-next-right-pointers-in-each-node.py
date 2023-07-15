# Definition for a Node.
from typing import Optional

class Node:
  def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next
        
class Solution:
  def connect(self, root: Optional[Node]) -> Optional[Node]:
    if not root:
      return
    root.next = None
    
    def dfs(node: Optional[Node]) -> Optional[Node]:
      if not node or not node.left:
        return
      node.left.next = node.right
      if node.next:
        node.right.next = node.next.left
      dfs(node.left)
      dfs(node.right)
        
    dfs(root)
    return root
  
    # def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    #     if( root == None ):
    #         return
    #     root.next = None
    #     def dfs(node):
    #         if( node == None or node.left == None ):
    #             return
    #         node.left.next = node.right
    #         if(node.next):
    #             node.right.next =node.next.left
    #         dfs(node.left)
    #         dfs(node.right)    

    #     dfs(root)
    #     return root
    # if root and root.left and root.right:
    #   left = self.connect(root.left)
    #   right = self.connect(root.right)
      
    #   left.next = right
      
    #   left.next = root.next.left
      # root
      # if left and right 
    
      # if root and root.next:
      #   nextRight = self.connect(root.next.left)
      #   right.next = nextRight
    # return root
  
    # def helper(root: Optional[Node]) -> Optional[Node]:
      

level2Node1 = Node(4)
level2Node2 = Node(5)
level2Node3 = Node(6)
level2Node4 = Node(7)

level1Node1 = Node(2, level2Node1, level2Node2)
level1Node2 = Node(3, level2Node3, level2Node4)

root = Node(1, level1Node1, level1Node2)

solution = Solution()
solution.connect(root)