from typing import List


class Solution:
  def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    dict = {}
    
    i = 0
    
    for i in range(0, len(list1)):
      if not dict.get(list1[i]):
        dict[list1[i]] = i
        
    minimumSum = 2002
    res = []
    for i in range(0, len(list2)):
      if dict.get(list2[i]) != None:
        if (i) + (dict.get(list2[i])) < minimumSum:
          minimumSum = (i) + (dict.get(list2[i]))
          res = [list2[i]]
        elif (i) + (dict.get(list2[i])) == minimumSum:
          res.append(list2[i])
    return res
        
solution = Solution()
print(solution.findRestaurant(["happy","sad","good"], ["sad","happy","good"]))