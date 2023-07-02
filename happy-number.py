class Solution:
  def isHappy(self, n: int) -> bool:
    
    hashset = set()
    
    res = 0
    while res != 1 and res not in hashset:
      hashset.add(res)
      res = 0
      exp=10
      while n > 0:
        res += pow(n%exp, 2)
        n//=exp
      n = res
    if res == 1:
      return True
    else:
      return False

    
solution = Solution()
print(solution.isHappy(2))