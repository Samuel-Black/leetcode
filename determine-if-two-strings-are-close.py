from collections import defaultdict


class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    n = len(word1)
    word1Freq = defaultdict(int)
    word2Freq = defaultdict(int)
    
    if n != len(word2):
      return False
    
    for i in range(0, n):
      word1Freq[word1[i]]+=1
      word2Freq[word2[i]]+=1
      
    temp = defaultdict(int)
    
    for char in word2Freq:
      temp[word2Freq[char]]+=1
    
    for char in word1Freq:
      if char not in word2Freq:
        return False
      if word1Freq[char] in temp:
        if temp[word1Freq[char]] == 1:
          del temp[word1Freq[char]]
        else:
          temp[word1Freq[char]]-=1

    return len(temp) == 0
      
    # temp = defaultdict(int)
    
    # for char in word2Freq:
    #   temp[word2Freq[char]]+=1
      
    # for char in word1Freq:
    #   if word1Freq[char] in temp:
    #     if temp[word1Freq[char]] == 1:
    #       del temp[word1Freq[char]]
    #     else:
    #       temp[word1Freq[char]]-=1
    #   else:
    #     return False
      
    # return len(temp) == 0
    
solution = Solution()
print(solution.closeStrings("abc", "bca"))
print(solution.closeStrings("a", "aa"))
print(solution.closeStrings("uau", "ssx"))