class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land=[]
        mini=float('inf')
        n=len(landStartTime)
        for i in range(n):
            land.append(landStartTime[i]+landDuration[i])
        land.sort()
        landcompleted=land[0]
        m=len(waterStartTime)
        for i in range(m):
            if waterStartTime[i]>=landcompleted:
                mini=min(mini,waterStartTime[i]+waterDuration[i])
            else:
                mini=min(mini,landcompleted+waterDuration[i])
        water=[]
        for i in range(m):
            water.append(waterStartTime[i]+waterDuration[i])
        water.sort()
        watercompleted=water[0]
        for i in range(n):
            if landStartTime[i]>=watercompleted:
                mini=min(mini,landStartTime[i]+landDuration[i])
            else:
                mini=min(mini,watercompleted+landDuration[i])
        return mini
        

        
