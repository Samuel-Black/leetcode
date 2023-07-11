class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    vowels = set(["a","e","i","o","u"])
    n = len(s)
    # start, end = 0, k - 1
    
    maxVowels = currentVowels = 0
    for i in range(0, k):
      if s[i] in vowels:
        currentVowels+=1
    maxVowels = currentVowels
    if maxVowels == k:
      return maxVowels
    
    for i in range(k, n):
      if s[i - k] in vowels:
        currentVowels-=1
      if s[i] in vowels:
        currentVowels+=1
      maxVowels = max(maxVowels, currentVowels)
      if maxVowels == k:
        return maxVowels
      
    return maxVowels
    
solution = Solution()
# print(solution.maxVowels("abciiidef", 3))
# print(solution.maxVowels("aeiou", 2))
# print(solution.maxVowels("leetcode", 3))
print(solution.maxVowels("zpuerktejfp", 3))