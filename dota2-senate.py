class Solution:
  def predictPartyVictory(self, senate: str) -> str:
    
    # queue = [s for s in senate]
    # rQueue = [i for i in enumerate(senate) if senate[i] == "R"]
    # dQueue = [i for i in enumerate(senate) if senate[i] == "D"]
    rQueue, dQueue = [], []
    n = len(senate)
    for i in range(0, n):
      if senate[i] == "R":
        rQueue.append(i)
      else:
        dQueue.append(i)
    
    while rQueue and dQueue:
      
      r = rQueue.pop(0)
      d = dQueue.pop(0)
      if r < d:
        rQueue.append(r+n)
      else:
        dQueue.append(d+n)
        
    return "Dire" if dQueue else "Radiant"

solution = Solution()
print(solution.predictPartyVictory("RD"))
print(solution.predictPartyVictory("RDD"))