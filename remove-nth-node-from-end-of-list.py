# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    count = 0
    left = head
    right = head
    
    while right:
      right = right.next
      count+=1
      if count > (n + 1):
        left = left.next
     
    if count == 0 and n == 1:
      head = None  
    elif count == n:
      head = left.next 
    elif count > n:
      left.next = left.next.next
      
    return head
  
# node4 = ListNode(5)
# node3 = ListNode(4, node4)
# node2 = ListNode(3, node3)
node1 = ListNode(2)
head = ListNode(1, node1)
solution = Solution()
res = solution.removeNthFromEnd(head, 1)
while res:
  print(res.val)
  res = res.next