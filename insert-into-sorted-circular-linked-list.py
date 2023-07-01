# Definition for a Node.
from typing import Optional


class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

      if head == None:
        newNode = Node(insertVal, None)
        newNode.next = newNode
        return newNode

      prev, curr = head, head.next
      toInsert = False

      while True:
        if prev.val <= insertVal <= curr.val:
          # Case #1.
          toInsert = True
        elif prev.val > curr.val:
          # Case #2. where we locate the tail element
          # 'prev' points to the tail, i.e. the largest element!
          if insertVal >= prev.val or insertVal <= curr.val:
            toInsert = True

        if toInsert:
          prev.next = Node(insertVal, curr)
          # mission accomplished
          return head

        prev, curr = curr, curr.next
        # loop condition
        if prev == head:
          break
      # Case #3.
      # did not insert the node in the loop
      prev.next = Node(insertVal, curr)
      return head
  
node2 = Node(5)
node1 = Node(3, node2)
head = Node(3, node1)
node2.next = head
# head.next = head
solution = Solution()
res = solution.insert(head, 0)

start = res
while res:
  print(res.val)
  res = res.next
  if res == start:
    break