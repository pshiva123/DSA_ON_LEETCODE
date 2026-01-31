class Solution:
    def reverseByType(self, s: str) -> str:
        i=0
        n=len(s)
        j=len(s)-1
        l=list(s.strip())
        while i<n and j>=0 and i<=j:
            if l[i].isalpha() and l[j].isalpha():
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            if i<n and not l[i].isalpha():
                i+=1
            if j>=0 and not l[j].isalpha():
                j-=1
        i=0
        j=n-1
        while i<=j:
            if (not l[i].isalpha()) and (not l[j].isalpha()):
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            if i<n and l[i].isalpha():
                i+=1
            if j>=0 and l[j].isalpha():
                j-=1
        return ''.join(l)
            
        
        
        
                
        
