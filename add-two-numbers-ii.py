import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    # l1Reversed = l1
    # l2Reversed = l2
    
    sum1 = 0
    sum2 = 0
    
    while l1:
      sum1*=10
      sum1+=l1.val
      l1 = l1.next
    
    while l2:
      sum2*=10
      sum2+=l2.val
      l2 = l2.next
        
    total = sum1 + sum2
    res = None
    
    while total > 0:
      res = ListNode((total % 10), res)
      total//=10
      
    return res if res else ListNode(0)
        
    
    # def reverseLinkedList(list: Optional[ListNode], reversedList: Optional[ListNode]):
    #   curr = list
    #   while l1:
    #     head = l1
        

l1c = ListNode(3)
l1b = ListNode(4, l1c)
l1a = ListNode(2, l1b)
l1 = ListNode(7, l1a)

l2b = ListNode(4)
l2a = ListNode(6, l2b)
l2 = ListNode(5, l2a)

solution = Solution()
print(solution.addTwoNumbers(l1, l2))