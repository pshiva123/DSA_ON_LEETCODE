from typing import List
import collections
import heapq

class Dsu:
    def __init__(self, n: int):
        self.p = list(range(n+1))
    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = Dsu(c)
        for u, v in connections:
            dsu.union(u, v)
        comp = collections.defaultdict(list)
        for station in range(1, c+1):
            root = dsu.find(station)
            comp[root].append(station)
        heaps = {}
        for root, members in comp.items():
            heapq.heapify(members)
            heaps[root] = members
        online = [True] * (c+1)
        ans = []
        for typ, x in queries:
            if typ == 1:
                if online[x]:
                    ans.append(x)
                else:
                    root = dsu.find(x)
                    h = heaps[root]
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    ans.append(h[0] if h else -1)
            else:
                online[x] = False  
        return ans

