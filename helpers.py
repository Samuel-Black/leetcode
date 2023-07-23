# helpers.py>
from typing import List

def arrayToLinkedList(arr: List, nodeClass):
  
  head = nodeClass()
  
  node = head
  for item in arr:
    node.next = nodeClass(item)
    node = node.next
  
  return head.next