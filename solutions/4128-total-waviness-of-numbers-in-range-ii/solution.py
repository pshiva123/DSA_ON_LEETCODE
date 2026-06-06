class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(pos, prev, prevprev, islimited,leadingzero,num,n,dp):
            if pos==n:
                return 1,0
            totalnumbers=0
            totalwavescore=0
            if (pos,prev,prevprev,islimited,leadingzero) in dp:
                return dp[(pos,prev,prevprev,islimited,leadingzero)]
            upto = 0
            if islimited:
                upto = int(num[pos])
            else:
                upto = 9   
            ans = 0
            for i in range(0, upto + 1):
                newleadingzero=True if (leadingzero and i==0) else False
                newprevprev=prev
                newprev=-1 if newleadingzero else i
                [remaintotalnumber,remaintotalwave]=solve(pos+1,newprev,newprevprev,(islimited and i==upto),newleadingzero,num,n,dp)
                if((not newleadingzero) and prevprev>=0 and prev>=0):
                
                    if (prev>prevprev and prev>i) or (prev<prevprev and prev<i) :
                        totalwavescore+=remaintotalnumber
                totalnumbers+=remaintotalnumber
                totalwavescore+=remaintotalwave
            dp[(pos,prev,prevprev,islimited,leadingzero)]=[totalnumbers,totalwavescore]
            return [totalnumbers,totalwavescore]







        if num2<100:
            return 0
        dp={}
        [totalnumbers,a]= solve(0, -1, -1,True,True,str(num2),len(str(num2)),dp)
        b=0
        dp={}
        if num1-1>100:
            [totalnumbers,b]=solve(0, -1, -1, True,True,str(num1-1),len(str(num1-1)),dp)

        return a - b
