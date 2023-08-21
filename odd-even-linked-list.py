# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    oddHead = ListNode()
    evenHead = ListNode()
    
    odd = oddHead
    even = evenHead
    
    node = head
    count = 0
    while node:
      if count % 2 == 0:
        even.next = node
        even = even.next
      else:
        odd.next = node
        odd = odd.next
      
      count+=1
      node = node.next
    
    odd.next = None
    even.next = oddHead.next
    
    return evenHead.next
    
    # node = head
    # even = ListNode
    # evenHead = even
    # if not head:
    #   return None
    # while node and node.next:
    #   even.next = node.next
    #   even = even.next
    #   node.next = node.next.next
    #   if node.next != None:
    #     node = node.next
    
    # even.next = None
    # node.next = evenHead.next
    # return head