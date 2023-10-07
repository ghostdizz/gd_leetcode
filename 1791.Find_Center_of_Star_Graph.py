from collections import defaultdict
from typing import List

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.find_num = -1
    
    def addEdge(self, u, v):
        self.g[u].append(v)

    def BFS(self, v):
        visited = [False] * (max(self.g)+1)
        queue = []
        queue.append(v)
        visited[v] = True
        if len(self.g[v]) == len(self.g)-1:
            self.find_num = v
            return 0
        while queue:
            v = queue.pop(0)
            for i in self.g[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] == True
                    if len(self.g[v]) == len(self.g)-1:
                        self.find_num = v
                        return 0

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = Graph()
        for i in range(2):
            graph.addEdge(edges[i][0], edges[i][1])
            graph.addEdge(edges[i][1], edges[i][0])
        graph.BFS(edges[0][0])
        return graph.find_num


