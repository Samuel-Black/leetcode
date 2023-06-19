from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node = head
    while node:
      nodeCompare = head
      while nodeCompare and node != nodeCompare:
        if node.val < nodeCompare.val:
          temp = node.val
          node.val = nodeCompare.val
          nodeCompare.val = temp
        nodeCompare = nodeCompare.next
      node = node.next
    
  # def insert_node(self, sorted_head, node):
  #   if not sorted_head or node.val < sorted_head.val:
  #     node.next = sorted_head
  #     sorted_head = node
  #   else:
  #     curr = sorted_head
  #     while curr.next and curr.next.val < node.val:
  #       curr = curr.next
  #     node.next = curr.next
  #     curr.next = node
    return head

n4 = ListNode(0)
n3 = ListNode(4, n4)
n2 = ListNode(3, n3)
n1 = ListNode(5, n2)
head = ListNode(-1, n1)

solution = Solution()
head = solution.insertionSortList(head)
node = head
while node != None:
  print(node.val)
  node = node.next
