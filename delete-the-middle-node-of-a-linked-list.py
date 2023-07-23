# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    node = head
    queue = []
    while node:
      queue.append(node)
      node = node.next
    
    middle = len(queue)//2
    
    if middle == 0:
      return None
    # if middle+1 == len(queue):
    #   queue[middle-1].next = None
    # else:
    queue[middle-1].next = queue[middle].next
    
    return head
    
solution = Solution()
print(solution.deleteMiddle())