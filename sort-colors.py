# 19/06/2023 come back later and solve again, solved in O(n^2) using selection sort due to tutorial

from typing import List

class Solution:
	def sortColors(self, nums: List[int]) -> None:
		numsLength = len(nums) - 1
		for i in range(numsLength):
			smallestIndex = i
			count = (i + 1)

			while count <= numsLength:
				if nums[count] < nums[smallestIndex]:
					smallestIndex = count
				# temp = nums[count] if temp < nums[count] else temp
				count+=1

			temp = nums[smallestIndex]
			nums[smallestIndex] = nums[i]
			nums[i] = temp

colors = [2,0,2,1,1,0]
solution = Solution()
solution.sortColors(colors)
print(colors)