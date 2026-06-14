class Solution:
    def getLength(self, nums: List[int]) -> int:
        ans,n=1,len(nums)
        for i in range(n):
            d={}
            freq={}
            d[nums[i]]=1
            freq[1]=1
            
            for j in range(i+1,n):
                
                if nums[j] not in d:
                    d[nums[j]]=1
                    freq[1]=freq.get(1,0)+1
                    
                else:
                    old=d[nums[j]]
                    freq[old]-=1
                    if freq[old]==0:
                        del freq[old]

                    d[nums[j]]+=1
                    new=d[nums[j]]
                    freq[new]=freq.get(new,0)+1
                    
                if len(freq)==2:
                    a,b=sorted(freq.keys())
                    if a<b:
                        a,b=b,a
                    if a==2*b:
                        ans=max(ans,j-i+1)
                        
                if len(d)==1:
                    ans=max(ans,j-i+1)
        return ans
                    
                    
                
        
