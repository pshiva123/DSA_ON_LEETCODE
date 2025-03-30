class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        curmin=cost[0]
        li=[curmin]
        for i in range(1,len(cost)):
            if cost[i]<curmin:
                curmin=cost[i]
            li.append(curmin)
        return li
        
