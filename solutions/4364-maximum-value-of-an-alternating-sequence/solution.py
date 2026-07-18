class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n==1:
            return s
        ans1=s+(n//2)*m-((n//2)-1)
        ans2=s+((n//2)-1) * m -(n//2)
        return max(ans1,ans2)
        
        
                
            
        
