from unittest import TestCase

class MyHashMap:

  def __init__(self):
    self.dict = {}

  def put(self, key: int, value: int) -> None:
    self.dict[key] = value

  def get(self, key: int) -> int:
    if key in self.dict:
      return self.dict[key]
    else:
      return -1

  def remove(self, key: int) -> None:
    if key in self.dict:
      del self.dict[key]
  # def __init__(self):
  #   self.map = [-1] * (pow(10,6) + 1)

  # def put(self, key: int, value: int) -> None:
  #   self.map[key] = value

  # def get(self, key: int) -> int:
  #   return self.map[key]

  # def remove(self, key: int) -> None:
  #   self.map[key] = -1

solution = MyHashMap()
testCase = TestCase()

solution.put(1,1)
solution.put(2,2)
solution.get(1)
solution.get(3)
solution.put(2,1)
solution.get(2)
solution.remove(2)
solution.get(2)