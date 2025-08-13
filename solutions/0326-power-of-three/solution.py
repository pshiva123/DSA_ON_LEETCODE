import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        exp=math.log(n,3)
        return 3**round(exp)==n
        
        


