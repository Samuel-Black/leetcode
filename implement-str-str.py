class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    res = -1
    left, right = 0, len(needle)
    
    while (right - 1) < len(haystack):
      if haystack[left] == needle[0] and haystack[right - 1] == needle[-1]:
        i = 0
        for i in range(0, len(needle)):
          if haystack[left + i] != needle[i]:
            break
        if i == len(needle) - 1:
          res = left
          return res
      left+=1
      right+=1
      
    return res
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))
print(solution.strStr("leetcode", "leeto"))
print(solution.strStr("hello", "ll"))
print(solution.strStr("a", "a"))
print(solution.strStr("abc", "c"))
print(solution.strStr("mississippi", "sipp"))