class Solution:
  def numJewelsInStones(self, jewels: str, stones: str) -> int:
    
    jewelsSet = set([x for x in jewels])
    
    count = 0
    for stone in stones:
      if stone in jewelsSet:
        count+=1
        
    return count
    
solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))