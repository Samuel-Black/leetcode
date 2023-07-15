# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    res = None
    prevSlow = head
    slow = head
    prevFast = head
    fast = head
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      
      if slow == fast:
        break
    
    if not fast or not fast.next:
      return None
    
    slow = head
    
    while slow != fast:
      fast = fast.next
      slow = slow.next
    
    return slow
solution = Solution()
print(solution.detectCycle())