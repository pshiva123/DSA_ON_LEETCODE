class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        return f(len(s),s,encCost,flatCost)


def f(l,curs,enc,flat):
    if l==0:
        return 0
    if l==1:
        if curs[0]=="1":
            return enc
        return flat
    x=0
    for i in range(l):
        if curs[i]=='1':
            x+=1
    cost=0
    if x==0:
        cost=flat
    else:
        cost=l*x*enc
    if l%2==0:
        idx=(l//2)-1
        a=f(l//2,curs[:idx+1],enc,flat)
        b=f(l//2,curs[idx+1:],enc,flat)
        return min(cost,a+b)
    return cost

