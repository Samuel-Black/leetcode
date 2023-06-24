# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      res = ListNode()
      head = res
      head1 = list1
      head2 = list2
      
      while head1 and head2:
        smallerHead = ListNode()
        
        if head1 and head2 and head1.val <= head2.val:
          smallerHead = head1
          head1 = head1.next
          
        elif head2:
          smallerHead = head2
          head2 = head2.next
          
        head.next = smallerHead
        head = head.next
        
      head.next = head1 if head1 is not None else head2
      
      return res.next