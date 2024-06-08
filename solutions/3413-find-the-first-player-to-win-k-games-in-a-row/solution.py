class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        if(k>=len(skills) or k>=10**5):
            return skills.index(max(skills))
        l1=[]
        for i in range(len(skills)):
            l1.append(i)
        #print(*l1)
        winct=int(0)
        while True:
            if(skills[l1[0]]>skills[l1[1]]):
                winct+=1
                loser=l1.pop(1)
                l1.append(loser)
            else:
                winct=1
                loser=l1.pop(0)
                l1.append(loser)
            if(winct==k):
                return l1[0]
                    

        
        
        
