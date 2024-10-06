class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        k=bin(nums[0])[2:]
        l=bin(nums[1])[2:]
        m=bin(nums[2])[2:]
        a=int(k+l+m,2)
        b=int(k+m+l,2)
        c=int(m+k+l,2)
        d=int(m+l+k,2)
        e=int(l+m+k,2)
        f=int(l+k+m,2)
        return max(a,b,c,d,e,f)

        
