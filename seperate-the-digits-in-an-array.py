from typing import List

class Solution:
  def separateDigits(self, nums: List[int]) -> List[int]:
    res=[]
    for num in nums:
      temp = []
      while num>0:
        temp.insert(0, num%10)
        num=num//10
      res += temp
    return res
    # res = []
    # for num in nums:
    #   numStr = str(num)
    #   for digit in numStr:
    #     res.append(int(digit))
        
    # return res
    
solution = Solution()
print(solution.separateDigits([13,25,83,77]))