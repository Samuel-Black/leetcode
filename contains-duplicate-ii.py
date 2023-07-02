from typing import List

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    
    dict = {}
    
    for i in range(0, len(nums)):
      if dict.get(nums[i]) == None:
        dict[nums[i]] = [i]
      else:
        dict[nums[i]].append(i)
        n = len(dict[nums[i]])
        for j in range(0, n):
          if j + 1 < n:
            distance = abs(dict[nums[i]][j] - dict[nums[i]][j+1])
            if distance <= k:
              return True

    return False
    
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))