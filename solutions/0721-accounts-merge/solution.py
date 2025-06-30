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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        dj=Disjointset(n)
        d={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in d:
                    d[accounts[i][j]]=i
                else:
                    par=d[accounts[i][j]]
                    dj.unionbysize(par,i)
        li=[[] for i in range(n)]
        for item in d:
            idx=dj.findPar(d[item])
            li[idx].append(item)
        for i in range(n):
            li[i].sort()
        ans=[]
        for i in range(n):
            if li[i]==[]:
                continue
            else:
                t=[accounts[i][0]]
                t+=li[i]
                ans.append(t)
        return ans


        
