from unittest import TestCase

class Solution:
  def winnerOfGame(self, colors: str) -> bool:

    dict = {
      "A": 0,
      "B": 0,
    }
    
    n = len(colors)
    
    for i in range(1, (n-1)):
      if colors[i] == colors[i-1] == colors[i+1]:
        dict[colors[i]]+=1
      
    return dict["A"] != 0 and dict["A"] > dict["B"]

solution = Solution()
testCase = TestCase()

test1 = solution.winnerOfGame("AAABABB")
testCase.assertEqual(test1, True)

test2 = solution.winnerOfGame("AA")
testCase.assertEqual(test2, False)

test3 = solution.winnerOfGame("ABBBBBBBAAA")
testCase.assertEqual(test3, False)