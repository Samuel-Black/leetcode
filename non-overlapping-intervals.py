from collections import defaultdict
from typing import List
import heapq

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    
    # sort by start time O(logn)
    intervals.sort(key=lambda x: x[1])
    deleted = 0
    overlap = -float('inf')
    
    for startTime, endTime in intervals:
      if startTime >= overlap:
        overlap = endTime
      else:
        deleted+=1
    return deleted
    # startTimes = [x[0] for x in intervals]
    # heapq.heapify(startTimes)
    # endTimes = [x[1] for x in intervals]
    # heapq.heapify(endTimes)
    
    # deleted = 0
    
    # while startTimes:
    #   startTime = heapq.heappop(startTimes)
      
    #   while startTime > endTimes[0]:
    #     heapq.heappop(endTimes)
    #     deleted+=1
    
    # overlaps = defaultdict(int)56
    
    # deleted = 0
    
    # for interval in intervals:
    #   start, end = tuple(interval)
      
    # if deleted == len(intervals):
    #   deleted-=1
    # return deleted
    
solution = Solution()
# print(solution.eraseOverlapIntervals([[1,3],[1,2],[2,3],[3,4]]))
# print(solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
# print(solution.eraseOverlapIntervals([[1,2],[2,3]]))
print(solution.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))