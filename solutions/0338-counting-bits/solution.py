class Solution:
    def countBits(self, n: int) -> List[int]:
        li=[]
        for i in range(n+1):
            k=bin(i)[2:].count("1")
            li.append(k)
        return li
        
