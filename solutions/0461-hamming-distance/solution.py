class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c=0
        while(x>0 or y>0):
            if x&1 != y&1:
                c+=1
            x=x>>1
            y=y>>1
        return c
        
