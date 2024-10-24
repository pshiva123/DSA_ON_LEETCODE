class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        ans=0
        for i in range(2**n):
            k=bin(i)[2:].zfill(n)
            print(k)
            x=0
            for j in range(len(k)):
                if k[j]=="1":
                    x=x^nums[j]
            ans+=x
        return ans
            
                
        
