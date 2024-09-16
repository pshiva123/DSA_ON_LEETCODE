class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mini=float('inf')
        timePoints.sort()
        n=len(timePoints)
        time=[0]*n
        for i in range(n):
            time[i]=(int(timePoints[i][:2])*60)+int(timePoints[i][3:])
        for i in range(n-1):
            if time[i]==0:
                k1=abs(1440-time[(i+1)])
                k2=abs(0-time[(i+1)])
                mini=min(mini,k1,k2)
            else:
                sub1=abs(time[i]-time[(i+1)])
                mini=min(mini,sub1)
        ans1=1440-time[-1]
        ans=ans1+time[0]
        mini=min(ans,mini)
        return mini



        return -1
        

        
