# Definition for singly-linked list.
from typing import Optional
from unittest import TestCase
from helpers import arrayToLinkedList

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
  
    sentinel = ListNode(0, head)
    reversedStart = None
    prev = sentinel
    node = head
    
    i = 1
    while i < left:
      prev = node
      node = node.next
      i+=1
      
    reversedStart = prev
    
    while i < right:
      newHead = node.next
      oldHead = reversedStart.next
      reversedStart.next = newHead
      node.next = newHead.next
      newHead.next = oldHead
      i+=1

      
    return sentinel.next
        
        
solution = Solution()
testCase = TestCase()


test1 = solution.reverseBetween(arrayToLinkedList([1,2,3,4,5], ListNode), 2, 4)

test2 = solution.reverseBetween(arrayToLinkedList([5], ListNode), 1, 1)