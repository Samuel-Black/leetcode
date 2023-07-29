from typing import List

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
    n = len(temperatures)
    res = [0]*n
    
    # stack of temperature and index in temperatures array
    stack = [(temperatures[-1], n-1)]
    
    # the last element is always 0, so start from the second last
    for i in range(n-2, -1, -1):
      if temperatures[i] < temperatures[i+1]:
        res[i] = 1
      else:
        for j in range(0, len(stack)):
          if temperatures[i] < stack[j][0]:
            res[i] = stack[j][1] - i
            break
        # j = i
        # while j < n - 1:
        #   if temperatures[i] < temperatures[j+1]:
        #     res[i] = (j+1) - i
        #     break
        #   j+=1
          # temperatures[i] < temperatures[i+1]
      stack.append((temperatures[i], i))
      stack.sort(key=lambda x: x[0])
    return res
    
solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(solution.dailyTemperatures([30,40,50,60]))
print(solution.dailyTemperatures([30,60,90]))