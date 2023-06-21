from typing import List

class Solution:
  def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
    # memory array to store the ordered array at index l, 
    # where the array stored contains the positition of the sorted integers of length l from the original nums array and is stored in memory[l]
    # this adds space but reduces complexity (re-sorting a length to get a different position for example)

    # test = "123456"
    # initialize an answer array which is length of queries
    # loop through len(queries) times 
    # during each iteration loop through nums 
    # return test[len(test) - 3:len(test)]
    
    # self.radix_sort(nums)
    numLength = len(nums[0])
    sortedArrays = [[] for _ in range(numLength)]
    # all strings in nums have same length with left padding 0's
    # loop through numLength times
    
    count = [[] for _ in range(10)]
    for i, num in enumerate(nums):
      
      numSplit = int(num[len(num) -1])
      # print(count[numSplit])
      count[numSplit].append(i)
    
    for sorted in count:
      if len(sorted) > 0:
        sortedArrays[0].extend(sorted)
        
    
    
    for i in range(1, numLength):
      # initialize count array for each new iteration
      count = [[] for _ in range(10)]
      
      previousSort = sortedArrays[i - 1]
      
      for sortedElem in previousSort:
        num = nums[sortedElem]
        numSplit = int(num[(len(num) - 1) - i])
        
        count[numSplit].append(sortedElem)
        
      for sorted in count:
        if len(sorted) > 0:
          sortedArrays[i].extend(sorted)
          
    answers = []
    for query in queries:
      
      k = query[0] - 1
      trim = query[1] - 1
      answers.append(sortedArrays[trim][k])
    return answers
      
      # loop through sorted Arrays, use i - 1 to access previous sort
      # for each previous element sort again using the second integer 
      # 
      # for j, num in enumerate(nums):
      #   numSplit = int(num[len(num) - (i + 1):len(num)-i])
      #   # print(count[numSplit])
      #   count[numSplit].append(j)

      
  #     for sorted in count:
  #       if len(sorted) > 0:
  #         sortedArrays[i].append(*sorted)
  #     # sort rightmost digit one at a time
  #     # at index 0 store an array of indexes in sorted order from the original nums array
  #     # continue onto index 1 using the sorted index at index 0 as reference for the next iteration of the radix sort
  #     # etc..
  #     # after first iteration 
      
      
  #   for i in range(0, len(queries)):
  #     k = queries[i][0]
  #     trim = queries[i][1]
      
  #     answer[i] = i
      
  #   return nums
  
  # def counting_sort(self, nums: List[int]) -> List[int]:
  #   counts = [] * 10
    
    
  # def counting_sort(self, lst: List[int], place_val: int, K: int = 10) -> List[int]:
  #   """
  #   Sorts a list of integers where minimum value is 0 and maximum value is K
  #   """
  #   # intitialize count array of size K
  #   counts = [0] * K

  #   for elem in lst:
  #     digit = (elem // place_val) % 10
  #     counts[digit] += 1

  #   # we now overwrite our original counts with the starting index
  #   # of each digit over our group of digits
  #   starting_index = 0
  #   for i, count in enumerate(counts):
  #     counts[i] = starting_index
  #     starting_index += count

  #   sorted_lst = [0] * len(lst)
  #   for elem in lst:
  #     digit = (elem // place_val) % 10
  #     sorted_lst[counts[digit]] = elem
  #     # since we have placed an item in index counts[digit],
  #     # we need to increment counts[digit] index by 1 so the
  #     # next duplicate digit is placed in appropriate index
  #     counts[digit] += 1

  #   return sorted_lst
  #   # common practice to copy over sorted list into original lst
  #   # it's fine to just return the sorted_lst at this point as well
  #   # for i in range(len(lst)):
  #   #   lst[i] = sorted_lst[i]

  # def radix_sort(self, lst: List[str], k = int) -> List[int]:
  #   # shift the minimum value in lst to be 0
  #   shift = min(lst)
  #   lst[:] = [num - shift for num in lst]
  #   max_elem = max(lst)

  #   # apply the radix sort algorithm
  #   place_val = 1
  #   while place_val <= max_elem:
  #     self.counting_sort(lst, place_val)
  #     place_val *= 10

  #   # undo the original shift
  #   lst[:] = [num + shift for num in lst]
      
    
solution = Solution()
# print(solution.smallestTrimmedNumbers(["102","473","251","814"], [[1,1],[2,3],[4,2],[1,2]]))
# print(solution.smallestTrimmedNumbers(["24","37","96","04"], [[2,1],[2,2]]))
print(solution.smallestTrimmedNumbers(["63050"], [[1,3],[1,5]]))
