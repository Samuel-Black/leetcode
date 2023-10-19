import itertools
from typing import List

class Solution:
  def tallestBillboard(self, rods: List[int]) -> int:
    sums = set(rods)
    largestSupport = 0
    
    # sum all combinations of array and store in set
    # while summing check if the sum exists in set,
    # if it does check if the current sum > largestSupport
    # and replace it if it is
    
    for size in range(1, len(rods)):
      # Iterate through all subsets of size "size"
      for subset in itertools.combinations(rods, size):
        subsetSum = sum(subset)
        if subsetSum in sums and subsetSum > largestSupport:
          largestSupport = subsetSum
        sums.add(subsetSum)
    
    return largestSupport
    
solution = Solution()
print(solution.tallestBillboard([1,2,3,6]))