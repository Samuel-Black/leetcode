from collections import defaultdict
import random


class RandomizedSet:

  def __init__(self):
    self.dict = {}
    self.arr = []

  def insert(self, val: int) -> bool:
    if val not in self.dict:
      # self.dict.get(val)s
      self.arr.append(val)
      i = (len(self.arr) - 1)
      self.dict[val] = i
      
      return True
    return False

  def remove(self, val: int) -> bool:
    if val in self.dict:
      # get the last element in the array and the index of the value to be deleted from the dictionary/hashmap
      lastElem = self.arr[-1]
      valIdx = self.dict[val]
      
      # set the value of the last element in the array to be index of the value to be deleted
      self.dict[lastElem] = valIdx
      
      # swap the last element in the array with the value to be deleted
      self.arr[valIdx] = lastElem
      self.arr[-1] = val
      
      # then remove the last element in the array since It's now the value to be deleted, and delete the key from the dictionary/hashmap
      self.arr.pop()
      del self.dict[val]
      return True
    return False

  def getRandom(self) -> int:
    return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(0))
print(obj.insert(0))
print(obj.insert(2))
print(obj.insert(3))
print(obj.remove(1))
print(obj.insert(3))
print(obj.insert(2))
# [3],[1],[],[3],[],[2]
# print(obj.insert(2))
# print(obj.insert(2))
# print(obj.insert(1))
# print(obj.insert(4))
# print(obj.remove(3))
# print(obj.remove(2))
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())

