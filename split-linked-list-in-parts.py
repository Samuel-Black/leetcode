# Definition for singly-linked list.
from typing import List, Optional
from unittest import TestCase
from helpers import arrayToLinkedList

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    cur = head
    for N in range(1001):
      if not cur: break
      cur = cur.next
    width, remainder = divmod(N, k)

    ans = []
    cur = head
    for i in range(k):
      head = cur
      for j in range(width + (i < remainder) - 1):
        if cur: cur = cur.next
      if cur:
        cur.next, cur = None, cur.next
      ans.append(head)
    return ans
        
    # # res = [[] for _ in range(0, k)]
    # nodes = []
    
    # node = head
    # while node:
    #   nodes.append(node)
    #   node = node.next
    
    # n = len(nodes)
    # res = []
    # i = 0
    # while k > 0:
    #   res.append([nodes[]])
      
    # return res
        
solution = Solution()
testCase = TestCase()

test1 = solution.splitListToParts(arrayToLinkedList([1,2,3], ListNode), 5)
# testCase.assertEqual(test1, [arrayToLinkedList([1], ListNode),arrayToLinkedList([2], ListNode),arrayToLinkedList([3], ListNode), [], []])

test2 = solution.splitListToParts(arrayToLinkedList([1,2,3,4,5,6,7,8,9,10], ListNode), 3)
# testCase.assertEqual(test2, [arrayToLinkedList([1,2,3,4], ListNode),arrayToLinkedList([5,6,7], ListNode),arrayToLinkedList([8,9,10], ListNode)])