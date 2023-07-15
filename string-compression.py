from typing import List

class Solution:
  def compress(self, chars: List[str]) -> int:
    
    # s = []
    # n = len(chars)
    i = 0
    
    while i < len(chars):
      charCount = 1
      currentChar = chars[i]
      while (i+1) < len(chars) and chars[i+1] == currentChar:
        chars.pop(i+1)
        charCount+=1
      if charCount > 1:
        count = 0
        while charCount > 0:
          chars.insert(i+1, str(charCount%10))
          charCount//=10
          count+=1
        i+=count
        # chars.insert(i+1, str(charCount))
      i+=1
    return len(chars)
    
solution = Solution()
# print(solution.compress(["a","a","b","b","c","c","c"]))
print(solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))