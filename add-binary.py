

class Solution:
  def addBinary(self, a: str, b: str) -> str:
    return bin(a) + bin(b)
    
solution = Solution()
print(solution.addBinary("11", "1"))