# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
  def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
      

solution = Solution()
testCase = TestCase()

test1 = solution.findInMountainArray([1,2,3,4,5,3,1], 3)
testCase.assertEqual(test1, 2)

test2 = solution.findInMountainArray([0,1,2,4,2,1], 3)
testCase.assertEqual(test2, -1)