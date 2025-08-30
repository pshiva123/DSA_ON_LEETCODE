class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s=str(n)
        c={}
        for i in s:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        temp=min(c.values())
        li=[]
        for i in c:
            if c[i]==temp:
                li.append(int(i))
        return min(li)
        
        
