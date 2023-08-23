from collections import Counter, defaultdict
import heapq
import unittest

class Solution:
  def reorganizeString(self, s: str) -> str:
    
      ans = []
      # Min heap ordered by character counts, so we will use
      # negative values for count
      pq = [(-count, char) for char, count in Counter(s).items()]
      heapq.heapify(pq)

      while pq:
        count_first, char_first = heapq.heappop(pq)
        if not ans or char_first != ans[-1]:
          ans.append(char_first)
          if count_first + 1 != 0: 
            heapq.heappush(pq, (count_first + 1, char_first))
        else:
          if not pq: return ''
          count_second, char_second = heapq.heappop(pq)
          ans.append(char_second)
          if count_second + 1 != 0:
            heapq.heappush(pq, (count_second + 1, char_second))
          heapq.heappush(pq, (count_first, char_first))

      return ''.join(ans)
    
    # if len(s) <= 0:
    #   return ""
    
    # freqMap = defaultdict(int)
    
    # for c in s:
    #   freqMap[c] += 1
    
    # priorityQueue = []
    
    # for c in freqMap:
    #   priorityQueue.append((freqMap[c], c))
    # priorityQueue.sort(reverse=True)
    
    # res = ""
    
    # # base case
    # item = priorityQueue[0]
    # res += item[1]
    # newItem = (item[0]-1, item[1])
    # if newItem[0] <= 0:
    #   priorityQueue.pop(0)
    # else:
    #   priorityQueue[0] = newItem
    
    # priorityQueue.sort(reverse=True)
    
    # while priorityQueue:
    #   if res[-1] == priorityQueue[0][1] and len(priorityQueue) <= 1:
    #     return ""
    #   elif len(priorityQueue) >= 2:
    #     item = priorityQueue[1]
    #     res += item[1]
    #     newItem = (item[0]-1, item[1])
    #     if newItem[0] <= 0:
    #       priorityQueue.pop(1)
    #     else:
    #       priorityQueue[0] = priorityQueue[1]
    #   else:
    #     item = priorityQueue[0]
    #     res += item[1]
    #     newItem = (item[0]-1, item[1])
    #     if newItem[0] <= 0:
    #       priorityQueue.pop(0)
    #     else:
    #       priorityQueue[0] = newItem
          
    #   priorityQueue.sort(reverse=True)
      
    # return res
        
solution = Solution()
test = unittest.TestCase()

test1 = solution.reorganizeString("aab")
test.assertEqual(test1, "aba")

test2 = solution.reorganizeString("aaab")
test.assertEqual(test2, "")