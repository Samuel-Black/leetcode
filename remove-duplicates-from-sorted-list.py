# Definition for singly-linked list.
from typing import Optional
from unittest import TestCase
from helpers import arrayToLinkedList

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    sortedHead = ListNode(-101)

    curr = head
    currSorted = sortedHead

    while curr:
      if curr.val != currSorted.val:
        currSorted.next = ListNode(curr.val, None)
        currSorted = currSorted.next

      curr = curr.next

    return sortedHead.next


solution = Solution()
testCase = TestCase()

test1 = solution.deleteDuplicates(arrayToLinkedList([1,1,2,3,3], ListNode))
testCase.assertListEqual(arrayToLinkedList([1,2,3], ListNode), test1)
