

class Solution:
  def reverseVowels(self, s: str) -> str:
    leftIndex = 0
    rightIndex = len(s) - 1
    vowelSet = set(["a","e","i","o","u","A","E","I","O","U"])
    res = list(s)
    while leftIndex < rightIndex:
      leftChar = s[leftIndex]
      rightChar = s[rightIndex]
      if leftChar in vowelSet and rightChar in vowelSet:
        res[leftIndex] = rightChar
        leftIndex += 1
        res[rightIndex] = leftChar
        rightIndex -= 1
      if leftChar not in vowelSet:
        res[leftIndex] = leftChar
        leftIndex += 1
      if rightChar not in vowelSet:
        res[rightIndex] = rightChar
        rightIndex -= 1
    return ''.join(res)
solution = Solution()
print(solution.reverseVowels(" "))
        
    