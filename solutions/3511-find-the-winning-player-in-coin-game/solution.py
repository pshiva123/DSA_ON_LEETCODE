class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        c=0
        while(x>0 and y>3):
            x-=1
            y-=4
            c-=1
        if(c%2==0):
            return "Bob"
        return "Alice"
            
        
