class Solution:
    def numTrees(self, n: int) -> int:
        k=math.factorial(n)
        l=math.factorial(2*n)
        m=math.factorial(n+1)
        return l//(k*m)
        
