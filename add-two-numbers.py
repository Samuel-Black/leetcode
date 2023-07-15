# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    leftOver = 0
    
    res = ListNode(0)
    resHead = res
    exp = 10
    while l1 or l2 or leftOver > 0:
      currSum = leftOver
      
      if l1:
        currSum += l1.val
        l1 = l1.next
      
      if l2:
        currSum += l2.val
        l2 = l2.next
    
      num = currSum % 10

      res.next = ListNode(num)
      res = res.next
      
      leftOver = currSum // exp

    return resHead if resHead.next is None else resHead.next

    # s1, s1Exp, s2, s2Exp = 0, 10, 0, 10
    
    # node1 = l1
    # node2 = l2
    # while node1 or node2:
    #   if node1:
    #     s1 *= s1Exp
    #     s1 += node1.val
    #     node1 = node1.next
    #   if node2:
    #     s2 *= s2Exp
    #     s2 += node2.val
    #     node2 = node2.next
        
    # listSum = s1 + s2
    
    # if listSum == 0:
    #   return ListNode(0)
    
    # exp = 1

    # res = None
    # resHead = None
    # while listSum // exp > 0:
    #   num = (listSum // exp) % 10
    #   if res is None:
    #     res = ListNode(num)
    #     resHead = res
    #   else:
    #     res.next = ListNode(num)
    #     res = res.next
    #   exp *= 10
    
    # return resHead
        
