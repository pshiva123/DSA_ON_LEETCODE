class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s=bin(start)[2:].zfill(32)
        g=bin(goal)[2:].zfill(32)
        c=0
        for i in range(32):
            if s[i]!=g[i]:
                c+=1
        return c
            
        
