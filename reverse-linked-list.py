# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    res = None
    node = head
    # 1 - 2 - 3 - 4 - 5
    while node and node:
      temp = node
      head = node.next
      node.next = res
      res = temp
      
      node = head
    return res
  
node4 = ListNode(5)
node3 = ListNode(4, node4)
node2 = ListNode(3, node3)
node1 = ListNode(2, node2)
head = ListNode(1, node1)
solution = Solution()
res = solution.reverseList(head)

while res:
  print(res.val)
  res = res.next
