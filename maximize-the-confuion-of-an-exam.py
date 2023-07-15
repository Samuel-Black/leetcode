class Solution:
  def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    
    # res = 0
    
    swappedToFCount = swappedToTCount = 0
    fSwapStartIndex = tSwapStartIndex = 0
    consecutiveFLength = consecutiveTLength = 0
    n = len(answerKey)
    
    for i in range(0, n):
      if answerKey[i] == "T" and swappedToFCount < k:
        swappedToFCount += 1
      elif answerKey[i] == "T" and swappedToFCount >= k:
        for j in range(fSwapStartIndex, (i + 1)):
          if answerKey[j] == "T":
            fSwapStartIndex = (j + 1)
            break
      if answerKey[i] == "F" and swappedToTCount < k:
        swappedToTCount += 1
      elif answerKey[i] == "F" and swappedToTCount >= k:
        for j in range(tSwapStartIndex, (i + 1)):
          if answerKey[j] == "F":
            tSwapStartIndex = (j + 1)
            break
      consecutiveFLength = max((i - fSwapStartIndex) + 1, consecutiveFLength)
      consecutiveTLength = max((i - tSwapStartIndex) + 1, consecutiveTLength)
      
    return max(consecutiveFLength, consecutiveTLength)
    
solution = Solution()
print(solution.maxConsecutiveAnswers("TTFF", 2))
print(solution.maxConsecutiveAnswers("TFFT", 1))
print(solution.maxConsecutiveAnswers("TTFTTFTT", 1))