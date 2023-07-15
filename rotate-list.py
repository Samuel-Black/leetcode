# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
      return None
    
    start = head
    end = head
    n = 1
    while end:
      if not end.next:
        end.next = start
        break
      end = end.next
      n += 1
    
    count = 0
    k%=n
    curr = head
    prev = None
    while count < (n - k) and k != 0:
      prev = curr
      curr = curr.next
      count+=1
    
    if prev:
      prev.next = None
    else:
      end.next = None
    return curr
    
    # n = 1
    # end = head
    # while end and end.next:
    #   end = end.next
    #   n+=1
      
    # k%=n
    
    # # rotate = None
    # count = 0
    # start = head
    # while count < (k - 1):
    #   start = 
    #   count+=1
    
    
    # map = []
    
    # curr = head
    # while curr:
    #   map.append(curr)
    #   curr = curr.next
    
    # n = len(map)
    
    # k%=n
    
    # map = [*map[k::], map[:k]]
    
    # for i in range(0, n - 1):
    #   map[i].next = map[i + 1]
    
    # map[-1].next = None
    
    # return map[0]
    
node4 = ListNode(5)
node3 = ListNode(4, node4)
node2 = ListNode(3, node3)
node1 = ListNode(2, node2)
head = ListNode(1, node1)
# node = ListNode(1)
# head = ListNode(2, node)
# node = ListNode(2)
# head = ListNode(1, node)
solution = Solution()
res = solution.rotateRight(head, 2)

while res:
  print(res.val)
  res = res.next


    # res = head
    
    # curr = head
    # count = 0
    # start, end = curr, curr
    # while curr:
    #   count+=1
    #   if not curr:
    #     curr = head
    #   curr = curr.next
    #   if curr:
    #     end = curr
    
    # k %= count
    # while count < k:
    #   end.next = start
      
    # return res