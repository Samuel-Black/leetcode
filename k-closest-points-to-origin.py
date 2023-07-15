import math
from typing import List
import heapq

class Node(object):
  def __init__(self, x: int, y: int, distance: float):
    self.x = x
    self.y = y
    self.distance = distance

  def __repr__(self) -> List[int]:
    return repr([self.x, self.y])

  def __gt__(self, other):
    return self.distance > other.distance

class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    maxHeap = []
    
    for point in points:
      currentMax = maxHeap[0].distance if maxHeap.__len__() > 0 else 0
      
      x = point[0]
      y = point[1]
      currentDistance = (x**2 + y**2) * -1
      
      if maxHeap.__len__() < k:
        heapq.heappush(maxHeap, Node(x, y, currentDistance))
      elif currentDistance > currentMax:
        heapq.heapreplace(maxHeap, Node(x, y, currentDistance))
      
    res = []
    for node in maxHeap:
      res.append([node.x, node.y])
    return res
  
solution = Solution()
print(solution.kClosest(
  [[3,3],[5,-1],[-2,4]],
  2
))

