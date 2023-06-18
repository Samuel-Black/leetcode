from typing import List
import heapq

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    startTimes = []
    endTimes = []
    
    roomCount = 0
    roomsRequired = 0
    
    for interval in intervals:
      startTime = interval[0]
      endTime = interval[1]
      heapq.heappush(startTimes, startTime)
      heapq.heappush(endTimes, endTime)
      
    while startTimes.__len__() > 0:
      startTime = heapq.heappop(startTimes)
      roomCount+=1

      while startTime >= endTimes[0]:
        heapq.heappop(endTimes)
        roomCount-=1
      
      roomsRequired = roomCount if roomCount > roomsRequired else roomsRequired
      
    return roomsRequired
    
    
solution = Solution()
print(solution.minMeetingRooms(
  [[9,10],[4,9],[4,17]]
  # [[1,5],[8,9],[8,9]]
  # [[1293,2986],[848,3846],[4284,5907],[4466,4781],[518,2918],[300,5870]]
))