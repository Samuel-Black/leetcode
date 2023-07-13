from collections import defaultdict
from typing import List


# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
    
class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
    courses = defaultdict(list)
    
    for course in prerequisites:
      courses[course[1]].append(course[0])
      
    for course in courses:
      current = course[0]
      count = 1
      while current:
        
      if count >= numCourses:
        return True
      
    return False
    
    
    
solution = Solution()
print(solution.canFinish(2, [[1,0]]))