from collections import defaultdict
from functools import cache
from unittest import TestCase

class Solution:
  def integerReplacement(self, n: int) -> int:
    
    # bottom up dp
    # dp = {
    #   n: 0
    # }
    dp = defaultdict(lambda: float('inf'))
    dp[n] = 0
    queue = [n]
    seen = set()
    while queue:
      num = queue.pop(0)
      if num % 2 == 0 and (num) > 0:
        dp[num/2] = min(dp[num/2], dp[num]+1)
        queue.append(num/2)
      else:
        dp[num-1] = min(dp[num-1], dp[num]+1)
        dp[num+1] = min(dp[num+1], dp[num]+1)
        if (num-1) not in seen and (num-1) > 0:
          queue.append(num-1)
        if (num+1) not in seen and (num+1) > 0:
          queue.append(num+1)
      seen.add(num)
        # if (n-1) in dp:
        #   dp[n-1] = min(dp[n-1], dp[n]+1)
        # else:
        #   dp[n-1] = dp[n]+1
        # if (n+1) in dp:
        #   dp[n+1] = min(dp[n+1], dp[n]+1)
        # else:
        #   dp[n-1] = dp[n]+1
        # n = min(dp[n+1], n[-1])
          
    return dp[1]
    # top down dp
    # @cache
    # def dp(n: int, operations: int):
    #   if n == 1:
    #     return operations
    #   if n%2 == 0:
    #     return dp(n/2, operations+1)
    #   else:
    #     return min(dp(n-1, operations+1), dp(n+1, operations+1))
    # return dp(n, 0)
    # queue = [(n, 0)]

    # while queue:
    #   num, operations = queue.pop(0)
    #   if num == 1:
    #     return operations
    #   if num % 2 == 0:
    #     queue.append(((num/2), (operations+1)))
    #   else:
    #     queue.append(((num-1), (operations+1)))
    #     queue.append(((num+1), (operations+1)))
    # # operations = 0
    # # while n > 1:
    # #   if n % 2 == 0:
    # #     n/=2
    # #   else:
    # #     if n > 3 and (n+1)%3 == 0:
    # #       n+=1
    # #     else:
    # #       n-=1
    # #   operations+=1
    # return -1

solution = Solution()
testCase = TestCase()

test1 = solution.integerReplacement(8)
testCase.assertEqual(test1, 3)

test2 = solution.integerReplacement(7)
testCase.assertEqual(test2, 4)

test3 = solution.integerReplacement(3)
testCase.assertEqual(test3, 2)

test4 = solution.integerReplacement(65535)
testCase.assertEqual(test4, 17)