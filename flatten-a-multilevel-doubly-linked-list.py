# Definition for a Node.
from typing import Optional


class Node:
  def __init__(self, val = 0, prev = None, next = None, child = None):
    self.val = val
    self.prev = prev
    self.next = next
    self.child = child

class Solution:
  def flatten(self, head: Optional[Node]) -> Optional[Node]:
    res = head
    if not head:
      return None
    else: 
      self.helper(head)
    return res
  def helper(self, head: Optional[Node]) -> Optional[Node]:
    curr = head
    if curr and curr.child:
      temp = curr.next
      currChild = self.helper(curr.child)
      if temp and temp.prev:
        temp.prev = currChild
        temp.prev.next = temp
      curr.next = curr.child
      curr.child.prev = curr
      curr.child = None

    if curr and curr.next is None:
      return curr
    else:
      return self.helper(curr.next)



level3Node = Node(12)
level3Head = Node(11, None, level3Node)
level3Node.prev = level3Head

level2Head = Node(7)
level2Node1 = Node(8, level2Head, None, level3Head)
level2Head.next = level2Node1
level2Node2 = Node(9, level2Node1)
level2Node1.next = level2Node2
level2Node3 = Node(10, level2Node2)
level2Node2.next = level2Node3

level1NodeHead = Node(1)
level1Node1 = Node(2, level1NodeHead)
level1NodeHead.next = level1Node1
level1Node2 = Node(3, level1Node1, None, level2Head)
level1Node1.next = level1Node2
# level1Node3 = Node(4, level1Node2)
# level1Node2.next = level1Node3
# level1Node4 = Node(5, level1Node3)
# level1Node3.next = level1Node4
# level1Node5 = Node(6, level1Node4)
# level1Node4.next = level1Node5

solution = Solution()
print(solution.flatten(level1NodeHead).val)
