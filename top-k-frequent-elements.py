from typing import List

class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		"""
		Sorts a list of integers using K buckets
		"""
		K = 15
		buckets = [[] for _ in range(K)]

		# place elements into buckets
		shift = min(nums)
		max_val = max(nums) - shift
		bucket_size = max(1, max_val / K)
		for i, elem in enumerate(nums):
			# same as k * nums[i] / max(nums)
			index = (elem - shift) // bucket_size
			# edge case for max value
			if int(index) == K:
				# put the max value in the last bucket
				buckets[K - 1].append(elem)
			else:
				buckets[int(index)].append(elem)

		res = []
		# sort individual buckets
		for i in range(0, k):
			res.append(buckets[i][0])
			# bucket.sort()

		# convert sorted buckets into final output
		# sorted_array = []
		# for bucket in buckets:
		# 	sorted_array.extend(bucket)

		# common practice to mutate original array with sorted elements
		# perfectly fine to just return sorted_array instead
		# for i in range(len(nums)):
		# 	nums[i] = sorted_array[i]
  
		return res
  
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([3,0,1,0], 1))
print(solution.topKFrequent([1,1,1,2,2,3333], 2))