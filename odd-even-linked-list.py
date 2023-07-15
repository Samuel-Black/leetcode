# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node = head
    even = ListNode
    evenHead = even
    if not head:
      return None
    while node and node.next:
      even.next = node.next
      even = even.next
      node.next = node.next.next
      if node.next != None:
        node = node.next
    
    even.next = None
    node.next = evenHead.next
    return head