class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        i=0
        j=0
        c=0
        while (i<n and j<m):
            if g[i]>s[j]:
                j+=1
            elif g[i]<=s[j]:
                i+=1
                j+=1
                c+=1
        return c
            
           
        
