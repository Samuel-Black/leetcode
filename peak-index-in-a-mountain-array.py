from typing import List
import heapq

class Node:
  def __init__(self, val, index):
    self.val = val
    self.index = index
    
  def __lt__(self, other):
    return self.val > other.val

class Solution:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    n = len(arr) - 1
    start, mid, end = 0, n//2, n
    while True:
      mid = (start + end) // 2
      if arr[mid-1] < arr[mid] > arr[mid+1]:
        return mid
      elif arr[mid-1] > arr[mid]:
        end = mid
      else:
        start = mid
        # mid = mid + mid//2
    # heap = []
    # for i in range(0 ,len(arr)):
    #   heap.append(Node(arr[i], i))
    
    
    # heapq.heapify(heap)
    
    # return heap[0].index
    
    
    # leftPeak, rightPeak = -1, (10**5) + 1
    # peakIndex = -1
    # left, right = 0 , len(arr)-1
    
    # while left <= right:
    #   if leftPeak < arr[left]:
    #     leftPeak = arr[left]
    #     left+=1
    #   elif leftPeak > arr[left]:
    #     if peakIndex == -1:
    #       peakIndex = left
    #     elif peakIndex != -1:
          
    #   if rightPeak > arr[right]:
    #     rightPeak = arr[right]
    #     right+=1
        
      
    #   left+=1
    #   right-=1
      

solution = Solution()
print(solution.peakIndexInMountainArray([0,1,0]))
print(solution.peakIndexInMountainArray([0,2,1,0]))
print(solution.peakIndexInMountainArray([0,10,5,2]))
print(solution.peakIndexInMountainArray([18,29,38,59,98,100,99,98,90]))
print(solution.peakIndexInMountainArray([3,4,5,1]))