from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    n =  len(digits) - 1
    for i in range(n, -1, -1):
      num = digits[i] + 1
      if num >= 10:
        digits[i] = 0
        if i == 0:
          digits.insert(0, 1)
      else:
        digits[i] = num
        break
    return digits
solution = Solution()
print(solution.plusOne([1,2,3]))
print(solution.plusOne([4,3,2,1]))
print(solution.plusOne([9]))