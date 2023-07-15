class Logger:

  def __init__(self):
    self.dict = {}

  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    if self.dict.get(message) == None or (self.dict.get(message) != None and timestamp >= self.dict[message]):
      self.dict[message] = (timestamp + 10)
      return True
    elif self.dict.get(message) != None and timestamp < (self.dict[message] + 10):
      return False


# Your Logger object will be instantiated and called as such:
obj = Logger()
print(obj.shouldPrintMessage(1,"foo"))
print(obj.shouldPrintMessage(10,"foo"))
print(obj.shouldPrintMessage(11,"foo"))