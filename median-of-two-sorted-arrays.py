from typing import List
from unittest import TestCase

class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    m = len(nums1)
    n = len(nums2)

    nums1Index = nums2Index = 0

    if (n + m) % 2 == 0:
      lastTwoNumbers = [0, 0]
      while (nums1Index + nums2Index) <= (n+m)/2:
        
        if nums1Index < m and nums2Index < n:
          if nums1[nums1Index] <= nums2[nums2Index]:
            lastTwoNumbers[0] = lastTwoNumbers[1]
            lastTwoNumbers[1] = nums1[nums1Index]
            nums1Index+=1
          else:
            lastTwoNumbers[0] = lastTwoNumbers[1]
            lastTwoNumbers[1] = nums2[nums2Index]
            nums2Index+=1
        else:
          if nums1Index >= m:
            lastTwoNumbers[0] = lastTwoNumbers[1]
            lastTwoNumbers[1] = nums2[nums2Index]
            nums2Index+=1
          else:
            lastTwoNumbers[0] = lastTwoNumbers[1]
            lastTwoNumbers[1] = nums1[nums1Index]
            nums1Index+=1
      return sum(lastTwoNumbers)/2
    else:
      median = -1
      while (nums1Index + nums2Index) <= (n+m)//2:
        if nums1[nums1Index] <= nums2[nums2Index]:
          median = nums1[nums1Index]
          nums1Index+=1
        else:
          median = nums2[nums2Index]
          nums2Index+=1
      return median


solution = Solution()
testCase = TestCase()

test1 = solution.findMedianSortedArrays([1,3], [2])
testCase.assertEqual(test1, 2.00000)

test2 = solution.findMedianSortedArrays([1,2], [3,4])
testCase.assertEqual(test2, 2.50000)