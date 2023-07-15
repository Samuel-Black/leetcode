class TwoSum:

  def __init__(self):
    self.nums = {}

  def add(self, number: int) -> None:
    if self.nums.get(number) == None:
      self.nums[number] = 1
    else:
      self.nums[number] += 1

  def find(self, value: int) -> bool:
    for num in self.nums:
      num2 = (value - num)
      if num == num2 and self.nums.get(num2) != None and self.nums.get(num2) >= 2:
        return True
      elif num != num2 and self.nums.get(num2) != None: 
        return True
    return False
  # def __init__(self):
  #   self.nums = {}
  #   self.sums = {}

  # def add(self, number: int) -> None:
  #   if self.nums.get(number) != None:
  #     self.sums[number*2] = True
  #   else:
  #     for num in self.nums:
  #       sum = (num) + (number)
  #       self.sums[sum] = True
  #     self.nums[number] = number

  # def find(self, value: int) -> bool:
  #   return self.sums.get(value) != None


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(1)
obj.add(3)
obj.add(4)
print(obj.find(4))
print(obj.find(7))
print(obj.find(10))