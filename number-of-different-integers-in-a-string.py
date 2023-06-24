class Solution:
  def numDifferentIntegers(self, word: str) -> int:
    num = ""
    numSet = set()
    for i in range(0, len(word)):
      if word[i].isdigit():
        num += word[i]
      else:
        if num != "":
          numSet.add(int(num))
          num = ""
    if num != "":
      numSet.add(int(num))
    return len(numSet)
    
solution = Solution()
print(solution.numDifferentIntegers("45uysad8sanskaj34dshajk45"))
print(solution.numDifferentIntegers("leet1234code234"))