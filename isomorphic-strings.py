class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    dictS = {}
    dictT = {}
    
    for i in range(0, len(s)):
      charS = s[i]
      charT = t[i]
      if charS not in dictS:
        dictS[charS] = charT
      if charT not in dictT:
        dictT[charT] = charS
      if dictS.get(charS) != charT or dictT.get(charT) != charS:
        return False
    
    return True
    
solution = Solution()
print(solution.isIsomorphic("egg", "add"))
print(solution.isIsomorphic("foo", "bar"))
print(solution.isIsomorphic("paper", "title"))
print(solution.isIsomorphic("badc", "baba"))