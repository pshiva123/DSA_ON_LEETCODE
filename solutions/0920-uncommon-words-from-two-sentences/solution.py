class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic={}
        s1=list(map(str,s1.split()))
        s2=list(map(str,s2.split()))
        for i in s1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in s2:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        li=[]
        for i in dic:
            if dic[i]==1:
                li.append(i)
        return li
        
