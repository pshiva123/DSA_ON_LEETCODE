class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n=len(nums)
        m=len(str(nums[0]))
        cnt=0
        for i in range(m):
            s={}
            for num in nums:
                digit=int(str(num)[i])
                if digit in s:
                    s[digit]+=1
                else:
                    s[digit]=1
            x=0
            for item in s:
                x+=s[item]*(n-s[item])
            cnt+=x
        return cnt//2
        
