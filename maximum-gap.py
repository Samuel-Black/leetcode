from typing import List
import sys

# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
# If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

class Solution:
  def maximumGap(self, nums: List[int]) -> int:
    if len(nums) <= 1:
      return 0
    
   # Find the maximum number in the array
    max_num = max(nums)

    # Perform radix sort
    exp = 1
    n = len(nums)
    sorted_nums = [0] * n

    while max_num // exp > 0:
        count = [0] * 10

        # Count the occurrences of each digit
        for num in nums:
            digit = (num // exp) % 10
            count[digit] += 1

        # Calculate the cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the sorted array
        i = n - 1
        while i >= 0:
            num = nums[i]
            digit = (num // exp) % 10
            index = count[digit] - 1
            sorted_nums[index] = num
            count[digit] -= 1
            i -= 1

        # Update the original array
        nums = sorted_nums[:]

        exp *= 10

    # Calculate the maximum difference between successive elements
    max_diff = 0
    for i in range(1, n):
        diff = nums[i] - nums[i - 1]
        max_diff = max(max_diff, diff)

    return max_diff
    # min = -sys.maxsize
    # max = sys.maxsize
    # countingSort = [0] * len(nums)
    
solution = Solution()
print(solution.maximumGap([3,6,9,1]))