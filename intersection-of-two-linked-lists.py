# Definition for singly-linked list.
from typing import Optional

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    
    nodeA = headA
    nodeB = headB
    
    while nodeA != nodeB:
      nodeA = headB if nodeA is None else nodeA.next
      nodeB = headA if nodeB is None else nodeB.next
    
    return nodeA
    # nodes = set()
    # iteration = 0
    
    # fast = headA
    # slow = headB
    
    # while fast and fast.next and iteration < 3:
    #   if not fast:
    #     headA
    #   if headA == headB:
    #     return headA
    #   headA = headA.next.next
      
    
    # while headA or headB:
    #   if headA:
    #     if headA in nodes:
    #       return headA
    #     nodes.add(headA)
    #     headA = headA.next
    #   if headB:
    #     if headB in nodes:
    #       return headB
    #     nodes.add(headB)
    #     headB = headB.next
    
    return None
    
    
solution = Solution()
print(solution.getIntersectionNode())