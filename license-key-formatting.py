

class Solution:
  def licenseKeyFormatting(self, s: str, k: int) -> str:
    n = len(s)
    currentSubstrLength = 0
    res = ""
    for i in range(n-1, -1, -1):
      if s[i] == "-":
        continue
      if currentSubstrLength == k:
        currentSubstrLength = 0
        res = "-" + res
      if currentSubstrLength < k:
        currentSubstrLength += 1
        res = s[i].capitalize() + res
        
    return res
    
solution = Solution()
# print(solution.licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(solution.licenseKeyFormatting("--a-a-a-a--", 2))
