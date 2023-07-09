from typing import List

class Solution:
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    
    bfs(rooms)
    
    # Function to print a BFS of graph
    def bfs(s):
 
      visited = []
      # Create a queue for BFS
      queue = []

      # Add the source node in
      # visited and enqueue it
      queue.append(s)
      visited.append(s)

      while queue:

        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        print (s, end = " ")

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then add it
        # in visited and enqueue it
        for i in rooms[s]:
          if i not in visited:
            queue.append(i)
            visited.append(s)