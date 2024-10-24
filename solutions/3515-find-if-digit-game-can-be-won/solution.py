class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1=0
        s2=0
        for i in nums:
            k=str(i)
            if len(k)==1:
                s1+=i
            else:
                s2+=i
        if s1==s2:
            return False
        return True
                
        
