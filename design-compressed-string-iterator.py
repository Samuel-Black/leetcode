from unittest import TestCase


class StringIterator:

  def __init__(self, compressedString: str):
    self.s = compressedString
    self.index = 0
    self.char = ''
    self.num = self.getNextNum()

  def next(self) -> str:
    res = ' '
    
    if self.hasNext():
      if self.num <= 0:
        self.num = self.getNextNum()

      res = self.char
    self.num-=1
    return res

  
  def getNextNum(self) -> int:
    if self.hasNext():
      num = 0
      i = self.index
      self.char = self.s[i]
      i+=1
      while i < len(self.s) and self.s[i].isnumeric():
        num*=10
        num += int(self.s[i])
        i+=1
      self.index = i
      return num
    
    return -1
  
  def hasNext(self) -> bool:
    return not (self.index >= len(self.s) and self.num <= 0)
      


# Your StringIterator object will be instantiated and called as such:
# compressedString = 'L10e2t1C1o1d1e11'
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()


methods = ["StringIterator","next","next","next","next","next","next","hasNext","next","hasNext"]
tests = [None,"L","L","L","L","L","L",True,"L",True]
params = [["L10e2t1C1o1d1e11"],[],[],[],[],[],[],[],[],[]]

solution = StringIterator(params[0][0])
testCase = TestCase()

for i in range(1, len(methods)):
  temp = getattr(solution, methods[i])
  res = temp()
  testCase.assertEqual(res, tests[i])