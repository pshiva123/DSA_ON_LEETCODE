class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return False if(str(n).count(str(x))==0 or str(n)[0]==str(x)) else True
        
