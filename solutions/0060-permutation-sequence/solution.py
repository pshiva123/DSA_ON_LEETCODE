from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        temp=permutations([v for v in range(1,n+1)])
        temp=sorted(list(temp))
        s=""
        for v in temp[k-1]:
            s+=str(v)
        return s

        
