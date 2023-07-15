from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    
    for i in range(0, len(nums)):
      hashmap[nums[i]] = i

    for i in range(0, len(nums)):
      key = (target) - (nums[i])
      index = hashmap.get(key)
      if index and i != index:
        return [i, index]
      
    return []
  
solution = Solution()
print(solution.twoSum([1,3,4,2], 6))