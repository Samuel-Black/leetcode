class RecentCounter:

  def __init__(self):
    self.queue = []
    
  def ping(self, t: int) -> int:
    self.queue.append(t)
    while self.queue and not (t - 3000 <= self.queue[0] <= t):
      self.queue.pop(0)
    return len(self.queue)
  
solution = RecentCounter()
print(solution.ping(1))
print(solution.ping(100))
print(solution.ping(3001))
print(solution.ping(3002))