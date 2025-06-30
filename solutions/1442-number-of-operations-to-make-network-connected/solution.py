class Disjointset:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*(n)
        self.count=0
    def findPar(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.findPar(self.parent[u])
        return self.parent[u]
    def unionbysize(self,u,v):
        ulp=self.findPar(u)
        vlp=self.findPar(v)
        if ulp==vlp:
            self.count+=1
            return
        elif self.size[ulp]<self.size[vlp]:
            self.parent[ulp]=vlp
            self.size[vlp]+=self.size[ulp]
        else:
            self.parent[vlp]=ulp
            self.size[ulp]+=self.size[vlp]

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n>len(connections)+1:
            return -1
        dj=Disjointset(n)
        temp=connections[0][0]
        for u,v in connections:
            dj.unionbysize(u,v)
        components=set()
        for i in range(n):
            x=dj.findPar(i)
            components.add(x)
        nl=len(components)-1
        # bcz we know the one component is fully connected and other need connection
        return nl if nl<=dj.count else -1

                
        
        
