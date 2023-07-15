# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    sentinel = ListNode(0, head)
    node = sentinel
    
    # while node and node.val == val:
    #   head = node.next
    #   node = head
    
    while node and node.next:
      if node.next.val == val:
        node.next = node.next.next
      else:
        node = node.next
    # while head:
    #   if head.val != val:
    #     if not res:
    #       res = head
    #     else:
    #       res.next = head
    #     res.next = None
        
    #     head = head.next
    #   head = head.next
    return sentinel.next
    
    
    

solution = Solution()
print(solution.removeElements())