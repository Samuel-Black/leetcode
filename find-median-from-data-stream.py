import heapq

class MedianFinder:

  def __init__(self):
    self.minHeap = []
    self.maxHeap = []

  def addNum(self, num: int) -> None:
    heapq.heappush(self.minHeap, -num)
    heapq.heappush(self.maxHeap, -self.minHeap[0])
    heapq.heappop(self.minHeap)
    
    if len(self.minHeap) < len(self.maxHeap):
      heapq.heappush(self.minHeap, -self.maxHeap[0])
      heapq.heappop(self.maxHeap)

  def findMedian(self) -> float:
    if len(self.minHeap) > len(self.maxHeap):
      return float(-self.minHeap[0])
    else:
      return (self.maxHeap[0] - self.minHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# medianFinder = MedianFinder()
# medianFinder.addNum(1)    
# medianFinder.addNum(2)    
# print(medianFinder.findMedian())
# medianFinder.addNum(3)    
# print(medianFinder.findMedian())

# medianFinder = MedianFinder()
# medianFinder.addNum(-1)  
# print(medianFinder.findMedian())  
# medianFinder.addNum(-2)
# print(medianFinder.findMedian())    
# medianFinder.addNum(-3)    
# print(medianFinder.findMedian())
# medianFinder.addNum(-4)    
# print(medianFinder.findMedian())
# medianFinder.addNum(-5)    
# print(medianFinder.findMedian())

medianFinder = MedianFinder()
medianFinder.addNum(6)  
print(medianFinder.findMedian())  
medianFinder.addNum(10)
print(medianFinder.findMedian())    
medianFinder.addNum(2)    
print(medianFinder.findMedian())
medianFinder.addNum(6)    
print(medianFinder.findMedian())
medianFinder.addNum(5)    
print(medianFinder.findMedian())
medianFinder.addNum(0)    
print(medianFinder.findMedian())
medianFinder.addNum(6)    
print(medianFinder.findMedian())
medianFinder.addNum(3)    
print(medianFinder.findMedian())
medianFinder.addNum(1)    
print(medianFinder.findMedian())
medianFinder.addNum(0)    
print(medianFinder.findMedian())
medianFinder.addNum(0)    
print(medianFinder.findMedian())