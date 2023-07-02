class Solution:
  def firstUniqChar(self, s: str) -> int:
    dict = {}
    
    for c in s:
      if dict.get(c) != None:
        dict[c] += 1
      else:
        dict[c] = 1
    
    for i in range(0, len(s)):
      if dict.get(s[i]) == 1:
        return i
    return -1
    
    
solution = Solution()
print(solution.firstUniqChar(""))