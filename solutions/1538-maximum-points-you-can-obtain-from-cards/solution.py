class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        s1=sum(cardPoints[0:k])
        ans=s1
        i=k-1
        j=n-1
        while(i>=0):
            s1-=cardPoints[i]
            s1+=cardPoints[j]
            j-=1
            i-=1
            ans=max(ans,s1)
        return ans
      
        




        
