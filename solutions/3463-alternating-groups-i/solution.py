class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n=len(colors);
        c=0
        for i in range(n):
            j=colors[i%n]
            k=colors[(i+1)%n]
            l=colors[(i+2)%n]
            if((j==l) and (k!=l)):
                c+=1
        return c
            
            
        
