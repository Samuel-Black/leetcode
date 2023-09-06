from typing import List
from unittest import TestCase

class Solution:
  def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
    # def binarySearch() -> int:
      
    
    n = len(nums1)
    res = [0] * n
    
    nums1.sort()
    nums2Sorted = [i[0] for i in sorted(enumerate(nums2), key=lambda x:x[1])]
    
    remainder = []
    j = 0
    
    while nums1 and nums1[0] < nums2[nums2Sorted[j]]:
      remainder.append((nums1.pop(0), nums2Sorted[j]))
      j+=1
      
    for i in range(0, n):
      if i < len(nums1):
        res[nums2Sorted[i]] = nums1[i]
      else:
        (num1, j) = remainder.pop(0)
        res[j] = num1
    
    return res
    
    
      
solution = Solution()
testCase = TestCase()

test1 = solution.advantageCount([2,7,11,15], [1,10,4,11])
testCase.assertEqual(test1, [2,11,7,15])

test2 = solution.advantageCount([12,24,8,32], [13,25,32,11])
testCase.assertEqual(test2, [24,32,8,12])

test3 = solution.advantageCount([15777,7355,6475,15448,18412], [986,13574,14234,18412,19893])
testCase.assertEqual(test3, [6475,15448,15777,18412,7355])