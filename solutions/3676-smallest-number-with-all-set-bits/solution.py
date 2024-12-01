class Solution:
    def smallestNumber(self, n: int) -> int:
        s=bin(n)
        bits=len(s)-2
        result=(1<<bits)-1
        return result
