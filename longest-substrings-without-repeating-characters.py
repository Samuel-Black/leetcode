class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    
    left, right = 0, 0
    
    prevChars = set()
    
    longestSubstr = 0
    
    n = len(s)
    
    if n <= 0:
      return 0
    
    while right < n:
      if s[right] not in prevChars:
        prevChars.add(s[right])
      else:
        while left < right:
          if s[left] == s[right]:
            left+=1
            break
          else:
            prevChars.remove(s[left])
            left+=1
      longestSubstr = (right - left) if (right - left) > longestSubstr else longestSubstr
      right+=1
      
    return longestSubstr + 1
    # longestSubStr = 0
    # count = 0
    
    # prevChars = {}
    
    # for str in s:
    #   if prevChars.get():
    #     count+=1
    #     prevChars[str] = count
    #   else:
    #     count=len(list(prevChars))
    #     prevChars.add(str)
    #   longestSubStr = count if count > longestSubStr else longestSubStr
      
    # return longestSubStr
    
solution = Solution()
print(solution.lengthOfLongestSubstring("aab"))
print(solution.lengthOfLongestSubstring("dvdf"))