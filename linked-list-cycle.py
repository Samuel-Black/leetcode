# Definition for singly-linked list.
from typing import Optional
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    # count = 0
    while slow and fast:
      slow = slow.next
      fast = fast.next
      if not fast:
        return False
      else: 
        fast = fast.next
      if slow == fast:
        return True
      
    return False
    
solution = Solution()
print(solution.hasCycle())