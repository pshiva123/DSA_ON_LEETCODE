from collections import deque
class Disjointset:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*(n)
    def findPar(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.findPar(self.parent[u])
        return self.parent[u]
    def unionbysize(self,u,v):
        ulp=self.findPar(u)
        vlp=self.findPar(v)
        if self.size[ulp]<self.size[vlp]:
            self.parent[ulp]=vlp
            self.size[vlp]+=self.size[ulp]
        else:
            self.parent[vlp]=ulp
            self.size[ulp]+=self.size[vlp]
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxrow,maxcol=0,0
        for i in stones:
            maxrow=max(maxrow,i[0])
            maxcol=max(maxcol,i[1])
        dj=Disjointset(maxrow+maxcol+2)
        #print(maxrow,maxcol)
        hashmap={}
        for i in stones:
            dj.unionbysize(i[0],i[1]+maxrow+1)
            hashmap[i[0]]=1
            hashmap[i[1]+maxrow+1]=1
        s=set()
        #print(hashmap)
        for temp in hashmap:
            x=dj.findPar(temp)
            s.add(x)
        return len(stones)-len(s)



             
