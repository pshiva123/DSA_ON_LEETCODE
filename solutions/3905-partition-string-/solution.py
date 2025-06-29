class Solution:
    def partitionString(self, s: str) -> List[str]:
        ss=set()
        li=[]
        i=0
        j=0
        n=len(s)
        while i<n and j<n:
            t=s[i:j+1]
            if t not in ss:
                li.append(t)
                ss.add(t)
                i=j+1
                j=j+1
            else:
                j+=1
        return li
            
            
        
