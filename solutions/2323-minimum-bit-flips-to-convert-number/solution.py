class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt=0
        for i in range(32):
            a=start>>i
            b=goal>>i
            if a&1 != b&1:
                cnt+=1
        return cnt

        
