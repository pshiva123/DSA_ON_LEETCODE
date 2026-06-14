class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        n=len(units[0])
        m=len(units)
        if m==1:
            return min(units[0])
        if n==1:
            x=0
            for i in units:
                x+=i[0]
            return x
        arr=[]
        for unit in units:
            arr.append(sorted(unit))
        ans=0
        mini=[]
        secondmini=[]
        for row in arr:
            mini.append(row[0])
            secondmini.append(row[1])
            ans+=row[0]
        minimum=min(mini)
        total_ans=0
        for i in range(m):
            total_ans+=(secondmini[i]-mini[i])
        way1=0
        for i in range(m):
            if mini[i]>minimum:
                way1+=secondmini[i]-mini[i]

        way2=total_ans-min(secondmini)+minimum

        return ans+max(way1,way2)
        
        
                
            
                
            
            
        
            
