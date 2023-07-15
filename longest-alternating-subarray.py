from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        currentLength = 0
        currentAlternates = []
        res = 0
        n = len(nums)
        
        i = 0
        while i < n:
          if i + 1 >= n:
            break
          else:
            if currentLength == 0 and nums[i] == (nums[i+1] - 1):
              currentLength+=2
              currentAlternates=[nums[i], nums[i+1]]
              i+=2
            elif currentLength >= 2 and [nums[i], nums[i + 1]] == currentAlternates:
              currentLength+=2
              i+=2
            else:
              if nums[i] == (nums[i+1] - 1):
                currentLength = 2
                currentAlternates=[nums[i],nums[i+1]]
                i+=2
              else:
                if currentLength == 2:
                  currentLength = 0
                  currentAlternates=[]
                  i-=1
                else:
                  currentLength = 0
                  currentAlternates=[]
                  i+=1
                # i-=1
          res = currentLength if currentLength > res else res
            

        return res if res > 0 else -1
      
solution = Solution()
print(solution.alternatingSubarray([2,3,4,3,4]))
print(solution.alternatingSubarray([31,32,31,32,33]))