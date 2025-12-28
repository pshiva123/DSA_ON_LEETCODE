import sys
sys.setrecursionlimit(10**6)
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costboth: int, need1: int, need2: int) -> int:
        a=need1*cost1+need2*cost2
        mini=min(need1,need2)
        b=mini*costboth+(-mini+need1)*cost1+(-mini+need2)*cost2
        c=max(need1,need2)*costboth
        return min(a,b,c)

        



        
