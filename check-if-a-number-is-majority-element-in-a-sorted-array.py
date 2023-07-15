from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    start, end, index = 0, len(nums) -1, len(nums)
    while start <= end:
      mid = (start + end) // 2
      if nums[mid] >= target:
        end = mid - 1
        index = mid
      else:
        start = mid + 1
    return index
  def isMajorityElement(self, nums: List[int], target: int) -> bool:
    n = len(nums)
    # if the middle index of the array doesn't equal the target,
    # since the array is in non decreasing order It's not possible
    # for the target to be the majority
    if nums[(n - 1) // 2] != target:
      return False
    
    startIndex = self.search(nums, target)
    endIndex = (n // 2) + startIndex
    return endIndex < n and nums[endIndex] == target
        
    
    
solution = Solution()
print(solution.isMajorityElement([2,4,5,5,5,5,5,6,6], 5))
print(solution.isMajorityElement([10,100,101,101], 101))
print(solution.isMajorityElement([2,5,5], 5))
print(solution.isMajorityElement([2,4,4,5,5,5,6,6,6], 5))
print(solution.isMajorityElement([1,2,2,3], 2))