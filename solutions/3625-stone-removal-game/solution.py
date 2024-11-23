class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        turn =True
        t=10
        while(n>=t):
            n=n-t
            t-=1
            turn = not turn
        return not turn
            
        
