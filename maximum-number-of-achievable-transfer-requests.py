from typing import List
class Solution:
  def __init__(self):
    self.ans = 0

  def helper(self, start, requests, indegree, n, count):
    if start == len(requests):
      for i in range(n):
        if indegree[i] != 0:
          return
      self.ans = max(self.ans, count)
      return

    # Take 
    indegree[requests[start][0]] -= 1
    indegree[requests[start][1]] += 1
    self.helper(start + 1, requests, indegree, n, count + 1)

    # Not-take
    indegree[requests[start][0]] += 1
    indegree[requests[start][1]] -= 1
    self.helper(start + 1, requests, indegree, n, count)

  def maximumRequests(self, n, requests):
    indegree = [0] * n
    self.helper(0, requests, indegree, n, 0)
    return self.ans
# class Solution:
#   def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
    
#     # buildingMap = [0] * n
#     # toBuildingMap = [0] * n
#     # prior = [0] * n
#     after = [0] * n
    
#     transfers = 0
    
#     # key being where they're from, value being where they're going
#     pendingTransferMap = {}
    
#     for i in range(0, n):
#       pendingTransferMap[i] = []
    
#     for request in requests:
#       # prior[request[0]] += 1
#       after[request[1]] += 1
      
#       # if the transfer is to the same building, It's always allowed and always counted
#       if request[0] == request[1]:
#         transfers+=1
      
#       # if the transfer is not to the same building
#       if request[0] != request[1]:
#         # if the building the employee wants to transfer to has an employee that wants to transfer out, this transfer is valid
#         if len(pendingTransferMap.get(request[1])) > 0:
#           transfers+=2
#           buildingLeft = pendingTransferMap.get(request[1]).pop()
#           if request[0] != buildingLeft:
#             pendingTransferMap[request[0]].append(request[0])
#         # if the transfer is not yet valid, put employee in the waitlist
#         else:
#           pendingTransferMap[request[0]].append(request[0])
#         # buildingMap[request[0]] -= 1
#         # toBuildingMap[request[1]]+=1
      
    
#     # difference = 0
#     # for i in range(0, len(buildingMap)):
#     #   difference += abs(abs(buildingMap[i]) - abs(toBuildingMap[i]))
#     # for i in range(0, len(prior)):
#     #   difference += abs(after[i] - prior[i])
#     return transfers
    # return int((len(requests) - abs(sum(buildingMap))))
    
solution = Solution()
print(solution.maximumRequests(5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))
print(solution.maximumRequests(3, [[0,0],[1,2],[2,1]]))
print(solution.maximumRequests(3, [[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]]))
print(solution.maximumRequests(3, [[0,0],[1,1],[0,0],[2,0],[2,2],[1,1],[2,1],[0,1],[0,1]]))