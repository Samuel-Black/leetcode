
# Definition for a Node.
from typing import Optional

class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random

class Solution:
  def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
    
    # copyHead = Node(0)
    
    # when there's a random, put the deep copy of that random node 

    node = head
    # node = head
    while node:
      node.next = Node(node.val, node.next, node.random)
      node = node.next.next
      # node = node.next
    
    resHead = Node(0)
    
    res = resHead
    
    node = head
    while node:
      res.next = node.next
      if node.next.random:
        res.next.random = node.next.random.next
      res = res.next
      node = node.next.next
      
    return resHead.next

    # res = Node(0)
    # resHead = res
    
    # curr = head
    # while curr:
    #   curr.next = Node(curr.val, curr.next, curr.random)
    #   curr = curr.next.next
    # # return head
  
    # curr = head
    # while curr:
    #   res.next = curr.next
    #   res.next.random = None if curr.next.random is None else curr.next.random.next
    #   res = res.next
    #   curr = curr.next.next
    # return resHead.next
    
    
node4 = Node(1)
node3 = Node(10, node4)
node2 = Node(11, node3)
node1 = Node(13, node2)
head = Node(7, node1)
node1.random = head
node2.random = node4
node3.random = node2
node4.random = head

solution = Solution()
copy = solution.copyRandomList(head)

while copy:
  print(copy.val)
  copy = copy.next