import itertools
from typing import List

class Solution:
  def putMarbles(self, weights: List[int], k: int) -> int:
    
    maxScore = -((2**31) - 1)
    minScore = (2**31) - 1
    
    def split():
      result = []
      # n-1 split points:
      for indices in itertools.combinations(range(1, len(weights)), k-1):
          # indices are the indices of split points
          splits = []
          start = 0
          for stop in indices:
            splits.append(weights[start : stop])
            start = stop
          splits.append(weights[start : ])
          result.append(splits)
      return result
    
    partitions = split()
    for partition in partitions:
      sum = 0
      for arr in partition:
        sum += arr[0] + arr[-1]
      maxScore = sum if maxScore < sum else maxScore
      minScore = sum if minScore > sum else minScore
    # for i in range(0, k):
    #   # [np.split(array, idx) 
    #   # for n_splits in range(5) 
    #   # for idx in combinations(range(1, len(array)), n_splits)]
    #   split(weights)
    #   for subset in itertools.combinations(weights, len(weights)):
    #     temp = subset
    return maxScore - minScore
    
solution = Solution()
print(solution.putMarbles([1,3,5,1], 2))