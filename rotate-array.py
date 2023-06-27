from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    # solution #1
    # for i in range(0, k):
    #   nums.insert(0, nums.pop())
    
    # solution #2
    n = len(nums)
    # mod k by length of the array to avoid pointless operations
    moves = k % n
    for i in range(0, moves):
      nums.insert(0, nums.pop())
      
    return nums

    
solution = Solution()
print(solution.rotate([1,2,3,4,5,6,7], 3))
print(solution.rotate([-1,-100,3,99], 2))