from typing import List

class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    
    end = len(nums)
    i = 0
    while i < end:
      if nums[i] == val:
        del nums[i]
        end -= 1
        i -= 1 if i > 0 else 0
      else:
        i += 1
        
    return len(nums)
  
solution = Solution()
print(solution.removeElement([1], 1))