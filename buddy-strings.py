class Solution:
  def buddyStrings(self, s: str, goal: str) -> bool:
    n = len(s)
    m = len(goal)
    # charToSwapIndex = -1
    
    sFrequencyMap = [0] * 26
    goalFrequencyMap = [0] * 26
    
    # goalFrequencyMap = {}
    
    if n != m:
      return False
    
    # if a string contains duplicate characters, but the strings are the same. return True
    
    # if a string does not contain duplicate characters and all characters in s[i] are the same as goal[i]. return False
    
    # if sSum == goalSum, and only two characters are out of place in the frequency map. return True
    differenceCount = 0
    largestFrequency = 0
    
    
    
    for i in range(0, len(goal)):
      sVal = ord(s[i]) % 26
      gVal = ord(goal[i]) % 26
      if s[i] != goal[i]:
        differenceCount+=1
      if differenceCount > 2:
        return False
        
      sFrequencyMap[sVal] += 1
      goalFrequencyMap[gVal] += 1
      largestFrequency = sFrequencyMap[sVal] if sFrequencyMap[sVal] > largestFrequency else largestFrequency
      # if goalFrequencyMap.get(s[i]) == None:
      #   goalFrequencyMap[s[i]] = 1
      # else:
      #   goalFrequencyMap[s[i]] += 1
      # if s[i] != goal[i] and charToSwapIndex == -1:
      #   charToSwapIndex = i
      # elif s[i] != goal[i] and charToSwapIndex != -1:
      #   if goal[charToSwapIndex] == s[i]:
      #     print(s[i::])
      #     print(goal[i::])
      #     if i < n - 1:
      #       return s[i::] == goal[i::]
      #     else:
      #       return True
      #   else:
      #     return False
    if differenceCount == 1 or differenceCount > 2:
      return False
    
    if differenceCount == 2 and sFrequencyMap == goalFrequencyMap:
      return True
    
    if differenceCount == 0 and largestFrequency >= 2:
      return True
    
    return False
      # sSum += ord(s[i])
      # goalSum += ord(goal[i])
      # if 
      # if 
      # if dict
      # dist = abs(ord(s[i]) - ord(goal[i]))
    
    # return sSum == goalSum
    
solution = Solution()
print(solution.buddyStrings("ab", "ba"))
print(solution.buddyStrings("aa", "aa"))
print(solution.buddyStrings("abab", "acaa"))