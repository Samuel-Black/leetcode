from typing import List
# import heapq
# from queue import PriorityQueue

class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    from heapq import heappush, heappop
    m = len(nums1)
    n = len(nums2)

    ans = []
    visited = set()

    minHeap = [(nums1[0] + nums2[0], (0, 0))]
    visited.add((0, 0))
    count = 0

    while k > 0 and minHeap:
      val, (i, j) = heappop(minHeap)
      ans.append([nums1[i], nums2[j]])

      if i + 1 < m and (i + 1, j) not in visited:
        heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
        visited.add((i + 1, j))

      if j + 1 < n and (i, j + 1) not in visited:
        heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
        visited.add((i, j + 1))
      k = k - 1
      
    return ans
    
    # q = PriorityQueue()
      
    # for num1 in nums1:
    #   for num2 in nums2:
    #     sum = (num1) + (num2)
    #     if len(q.queue) < k:
    #       q.put((-sum, [num1, num2]))
    #     elif -q.queue[0][0] > sum:
    #       q.get()
    #       q.put((-sum, [num1, num2]))
    #     elif num1 + nums2[0] > -q.queue[0][0]:
    #       break
          
    # return [x[1] for x in q.queue]
    
    
    # while len(res) < k and len(res) != len(nums1) * len(nums2):
    #   # while num1 < nums2
    #   # num2 += 1
    #   # if right > len()
      
    #   if right >= len(nums2):
    #     right -=1
    #     while len(res) < k:
    #       if len(res) == k or len(res) == len(nums1) * len(nums2):
    #         return res
    #       left+=1
    #       res.append([nums1[left], nums2[right]])
          
      
    #   while left < len(nums1) and right < len(nums2) and nums1[left] <= nums2[right]:
    #     if len(res) == k or len(res) == len(nums1) * len(nums2):
    #       return res
    #     res.append([nums1[left], nums2[right]])
    #     left+=1
      
    #   while left < len(nums1) and right < len(nums2) and nums2[right] <= nums1[left]:
    #     if len(res) == k or len(res) == len(nums1) * len(nums2):
    #       return res
    #     res.append([nums1[left], nums2[right]])
    #     right+=1
        
    # return res
      # if len(nums1) > left and nums1[left] <= nums2[right]:
      #   for i in range((left + right), min(right + 1, len(nums2))):
      #     if len(nums2) <= i:
      #       break
      #     res.append([nums1[left], nums2[i]])
      #     if len(res) == k:
      #       return res
      #   left+=1
      # elif len(nums2) > right:
      #   for i in range((left + right), min((left) + 1, len(nums1))):
      #     if len(nums1) <= i:
      #       break
      #     res.append([nums1[i], nums2[right]])
      #     if len(res) == k:
      #       return res
      #   right+=1
        
    # return res
    # q = PriorityQueue()
    
    # for num1 in nums1:
      
    #   for num2 in nums2:
    #     numSum = num1 + num2
    #     if len(q.queue) < k:
    #       q.put((numSum, [num1, num2]))
    #     elif q.queue[-1][0] > numSum:
    #       q.queue.pop()
    #       q.put((numSum, [num1, num2]))
    #     # if len(minHeap) < k:
    #     #   heapq.heappush(minHeap, Node([num1, num2], numSum))
    #     # elif -minHeap[0].sum > numSum:
    #     #   heapq.heapreplace(minHeap, Node([num1, num2], numSum))
  
    # # while minHeap:
    # #   res.append(heapq.heappop(minHeap).nums)
    # # res.reverse()
    # res = []
    # for i in range(0, len(q.queue)):
    #   res.append(q.queue[i][1])
    # return res
    
    # heapq.heapify(nums1)
    # heapq.heapify(nums2)
    
    # res = []
    # while len(res) < k:
    #   num1 = heapq.heappop(nums1)
    #   for i in range(0, len(nums2)):
    #     if len(res) == k:
    #       return res
    #     else:
          
    # return res
solution = Solution()
# print(solution.kSmallestPairs([1,7,11], [2,4,6], 3))
# print(solution.kSmallestPairs([1,1,2], [1,2,3], 2))
# print(solution.kSmallestPairs([1,2], [3], 3))
print(solution.kSmallestPairs([-10,-4,0,0,6], [3,5,6,7,8,100], 10))