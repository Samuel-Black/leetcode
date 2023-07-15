from typing import List


class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    dict = {}
    
    for num in nums1:
      if dict.get(num) != None:
        dict[num] += 1
      else:
        dict[num] = 1
     
    res = []
    for num in nums2:
      if dict.get(num) != None and dict.get(num) > 0:
        dict[num]-=1
        res.append(num)
    return res
    # return nums1
    
solution = Solution()
print(solution.intersect([1,2,2,1], [2,2]))