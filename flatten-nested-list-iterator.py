# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """

#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """

#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
  def __init__(self, nestedList: [NestedInteger]):
    self.flattenedList = []
    self.flattenList(nestedList)
  
  def flattenList(self, nestedList: [NestedInteger]):
    for i in nestedList:
      if i.isInteger():
        self.flattenedList.append(i.getInteger())
      else:
        self.flattenList(i.getList())
    
      
  def next(self) -> int:
    return self.flattenedList.pop(0)
      
  def hasNext(self) -> bool:
    return len(self.flattenedList) > 0