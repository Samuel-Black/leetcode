
# Definition for a Node.
from typing import Optional

class Node:
  def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next

class Solution:
  def connect(self, root: 'Node') -> 'Node':

    left = root.left
    while left:
      
    right = root.right
    while right:
      

level2Node1 = Node(4)
level2Node2 = Node(5)
level2Node4 = Node(7)

level1Node1 = Node(2, level2Node1, level2Node2)
level1Node2 = Node(3, None, level2Node4)

root = Node(1, level1Node1, level1Node2)

solution = Solution()
solution.connect(root)