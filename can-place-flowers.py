from typing import List

class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    k = len(flowerbed)
    
    count = 0
    i = 0
    while i < k:
      left = max(i-1, 0)
      right = min(i+1, (k-1))
      if flowerbed[left] == 0 and flowerbed[right] == 0 and flowerbed[i] == 0:
        count+=1
        i+=2
      else:
        i+=1
      if count >= n:
        return True
        
    return count >= n
    # i = count = 0
    
    # right
    
    # while i < k:
    #   if i == 0 and (flowerbed[i] == 0 or flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
    #     count+=1
    #   else:
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # k = len(flowerbed)
    # i = 0
    # count = 0
    # # skip first and last iteration
    # while i < k:
    #   if flowerbed[i] == 0 and ((i-1) < 0 or flowerbed[i - 1] == 0) and ((i + 1) > (k - 1) or flowerbed[i + 1] == 0):
    #     count += 1
    #     i += 2
    #   else: 
    #     i += 1
    # return count >= n
    
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1,1,1,1,1,1], 1))
print(solution.canPlaceFlowers([1,0,0,0,1,0,0], 2))
