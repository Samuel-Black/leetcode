class ListNode:
  def __init__(self, val=0, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

class MyLinkedList:

  def __init__(self):
    self.head = None

  def get(self, index: int) -> int:
    count = 0
    curr = self.head
    while count < index and curr:
      count+=1
      curr = curr.next
    return -1 if not curr else curr.val
  
  def addAtHead(self, val: int) -> None:
    temp = self.head
    self.head = ListNode(val, self.head)
    if temp:
      temp.prev = self.head
  
  def addAtTail(self, val: int) -> None:
    if not self.head:
      self.addAtHead(val)
      return
    curr = self.head
    while curr and curr.next:
      curr = curr.next
    curr.next = ListNode(val, None, curr)

  def addAtIndex(self, index: int, val: int) -> None:
    if not self.head and index == 0:
      self.addAtHead(val)
      return
    
    prev = self.head
    curr = self.head
    count = 0
    while count < index and curr:
      prev = curr
      curr = curr.next
      count+=1
    if count == index:
      if index == 0:
        temp = self.head
        self.head = ListNode(val, self.head)
        temp.prev = self.head
      else:
        prev.next = ListNode(val, curr, prev)
    
  def deleteAtIndex(self, index: int) -> None:
    if not self.head and not self.head.next:
      return
    prev = self.head
    curr = self.head
    count = 0
    while count < index and curr:
      prev = curr
      curr = curr.next
      count+=1
    if count == index:
      if index == 0:
        self.head = curr.next
      prev.next = None if not curr or not curr.next else curr.next
      if curr:
        curr.prev = prev

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# obj.addAtHead(7)
# obj.addAtHead(1)
# obj.addAtIndex(3,0)
# obj.deleteAtIndex(2)
# obj.addAtHead(6)
# obj.addAtTail(4)
# obj.get(4)
# obj.addAtHead(4)
# obj.addAtIndex(5,0)
# obj.addAtHead(6)
# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

# param_1 = obj.get(1)
# obj.addAtIndex(1,0)
# print(obj.get(0))
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# print(obj.get(1))
# obj.deleteAtIndex(0)
# print(obj.get(0))
obj.addAtIndex(0,10)
obj.addAtIndex(0,20)
obj.addAtIndex(1,30)
# obj.addAtIndex(0, 20)
print(obj.get(0))
# obj.addAtIndex(0,10)
# print(obj.get(0))
# print(obj.get(1))
# obj.addAtIndex(1,30)
# obj.addAtIndex(0,10)
# print(obj.get(0))
# print(obj.get(1))
# print(obj.get(2))
# print(obj.get(1))
# print(obj.get(2))
# print(obj.get(0))
# obj.addAtTail(4)
# obj.addAtIndex(2,3)
# obj.deleteAtIndex(2)