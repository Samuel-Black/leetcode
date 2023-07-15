class MovingAverage:

  def __init__(self, size: int):
    self.len = size
    self.arr = [0] * size
    self.index = 0
    self.count = 0
    self.sum = 0
    
  def next(self, val: int) -> float:
    if self.count < self.len:
      self.sum += val
    else:
      self.sum -= self.arr[self.index]
      self.sum += val
    self.arr[self.index] = val
    self.index = ((self.index + 1) % self.len)
    self.count = min(self.len, (self.count + 1))
    return self.sum / self.count


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))