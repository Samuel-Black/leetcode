from functools import cache
from typing import List

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # @cache
    # def binarySearch(nums: List[int], target: int) -> int:
    #   start, end, index = 0, len(nums) -1, len(nums)
    #   while start <= end:
    #     mid = (start + end) // 2
    #     if nums[mid] >= target:
    #       end = mid - 1
    #       index = mid
    #     else:
    #       start = mid + 1
    #   return index
    
    res = []
    
    map = {}
    
    for i in range(0, len(nums2)):
      map[i] = nums2[i]
    
    for num in nums1:
      index = map[i]
      heap = nums2[index:]

    return res