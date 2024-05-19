class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        li=[]
        i=0
        d=len(s)
        for ele in s:
            if(ele=="I"):
                li.append(i)
                i+=1
            else:
                li.append(d)
                d-=1
        for i in range(len(s)+1):
            if i not in li:
                li.append(i)
        return li                    
        
