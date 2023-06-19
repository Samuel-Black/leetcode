# 19/06/2023 come back later and solve again, solved in O(n^2) using selection sort due to tutorial

from typing import List

MAX_NUMS_LENGTH = 300

class Solution:
	def sortColors(self, nums: List[int]) -> None:
		numsCount = [0] * MAX_NUMS_LENGTH
		
		for num in nums:
			numsCount[num] += 1
  
		count = 0
		for i, num in enumerate(numsCount):
			for j in range (0, num):
				nums[count] = i
				count+=1
				# numsSorted.append(i)
			# insertedCount = 0
			# currentIndex = 0
			# while insertedCount < num:
			# 	lastIndex = index + insertedCount
			# 	nums[lastIndex] = index
			# 	insertedCount+=1
    
		# nums = numsSorted
		# numsLength = len(nums) - 1
		# for i in range(numsLength):
		# 	smallestIndex = i
		# 	count = (i + 1)

		# 	while count <= numsLength:
		# 		if nums[count] < nums[smallestIndex]:
		# 			smallestIndex = count
		# 		# temp = nums[count] if temp < nums[count] else temp
		# 		count+=1

		# 	temp = nums[smallestIndex]
		# 	nums[smallestIndex] = nums[i]
		# 	nums[i] = temp

colors = [2,0,2,1,1,0]
# colors = [2]
solution = Solution()
solution.sortColors(colors)
print(colors)