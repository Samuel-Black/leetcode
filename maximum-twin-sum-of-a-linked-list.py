# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
from typing import Optional
from helpers import arrayToLinkedList

class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    
    maxPair = 0
    slow = head
    fast = head
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    
    
    # node = head
    
    # while node:
    #   temp = node
    #   node = node.next
    #   temp.next = reversed
    #   reversed = temp
    reversed = None
    node = slow
    while node:
      temp = node
      node = node.next
      temp.next = reversed
      reversed = temp
    
    node = head
    
    while node and reversed:
      maxPair = max(node.val + reversed.val, maxPair)
      node = node.next
      reversed = reversed.next
    return maxPair
    # arr = []
    
    # node = head
    # while node:
    #   arr.append(node.val)
    #   node = node.next
    
    # left, right = 0, len(arr) - 1
    # maxPair = 0
    # while left < right:
    #   maxPair = max(arr[left] + arr[right], maxPair)
    #   left+=1
    #   right-=1
    
    # return maxPair


head = arrayToLinkedList([5,4,2,1], ListNode)
solution = Solution()
print(solution.pairSum(head))