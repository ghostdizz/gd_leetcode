from typing import List
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.a = False
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, source, destination):
        visited = {}
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:

            source = queue.pop(0)
            for i in self.graph[source]:
                if i not in visited:
                    if i == destination:
                        self.a = True
                        return
                    queue.append(i)
                    visited[i] = True

    
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        graph = Graph()
        for lst in edges:
            graph.graph[lst[0]].append(lst[1])
            graph.graph[lst[1]].append(lst[0])
        graph.BFS(source, destination)
        return graph.a
    
