class MyCircularQueue:

  def __init__(self, k: int):
    self.arr = [0] * k
    self.len = k
    self.start = self.end = -1

  def enQueue(self, value: int) -> bool:
    # if self.end == self.start:
    #   return False
    if self.isFull():
      return False
    elif self.start == self.end == -1:
      self.start = self.end = 0
    self.arr[self.end] = value
    self.end = ((self.end + 1) % self.len)
    return True

  def deQueue(self) -> bool:
    if self.isEmpty():
      return False
    self.start = ((self.start + 1) % self.len)
    if self.start == self.end:
      self.start = self.end = -1
    return True
    
  def Front(self) -> int:
    if self.isEmpty():
      return -1
    return self.arr[self.start]

  def Rear(self) -> int:
    if self.isEmpty():
      return -1
    if self.end - 1 < 0:
      return self.arr[self.len - 1]
    else:
      return self.arr[self.end-1]

  def isEmpty(self) -> bool:
    return self.start == -1 and self.end == -1

  def isFull(self) -> bool:
    return self.start != -1 and self.end != -1 and self.start == self.end


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.enQueue(4))
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.enQueue(4))
print(obj.enQueue(4))
print(obj.deQueue())
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.enQueue(4))
print(obj.deQueue())
print(obj.Rear())
print(obj.isFull())