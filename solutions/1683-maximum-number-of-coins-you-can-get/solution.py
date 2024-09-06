class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(*piles)
        k=len(piles)//3
        i=len(piles)-2
        s=0
        while(i>=k):
            s+=piles[i]
            i-=2
        return s


