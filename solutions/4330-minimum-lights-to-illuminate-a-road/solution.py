class Solution:
    def minLights(self, lights: list[int]) -> int:
        n=len(lights)
        left=[False]*n
        right=[False]*n
        cur=0
        for i in range(n):
            if lights[i]>0:
                cur=max(lights[i],cur-1)
                cur=max(0,cur)
                left[i]=True
            else:
                if cur>0:
                    cur=cur-1
                    left[i]=True
        cur=0
        for i in range(n-1,-1,-1):
            if lights[i]>0:
                cur=max(lights[i],cur-1)
                cur=max(0,cur)
                right[i]=True
            else:
                if cur>0:
                    cur=cur-1
                    right[i]=True
        ill=[False]*n
        for i in range(n):
            ill[i]=left[i] or right[i]
        x=ill.count(True)
        if x==0:
            return (n+2)//3
            
        ans=0
        print(*ill)
        illindices=[i+1 for i in  range(n) if ill[i]==True]
        ans+=(illindices[0]+1)//3
        for i in range(len(illindices)-1):
            tt=illindices[i+1]-illindices[i]-1
            ans+=(tt+2)//3
        ans+=(n-illindices[-1]+2)//3
        return ans
                    
            
            
            
                    
        
        
