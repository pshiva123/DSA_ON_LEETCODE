class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if i<=2:
                ans.append(-1)
            else:
                temp=bin(i)[2:]
                cur=float('inf')
                for j in range(len(temp)):
                    put="1"
                    if temp[j]=="1":
                        put="0"
                    x=int(temp[:j]+put+temp[j+1:],2)
                    if x | x+1 ==i:
                        cur=min(cur,x)
                if cur!=float('inf'):
                    ans.append(cur)
                else:
                    ans.append(-1)
                        
            
        return ans
        
