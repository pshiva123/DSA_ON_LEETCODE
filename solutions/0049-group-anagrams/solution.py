class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li=[]
        emp=[]
        for i in strs:
            l=list(i)
            l.sort()
            ll="".join(l)
            li.append(ll)
        #print(*li)
        s=set(li)
        lis=list(s)
        #print(*lis)
        for i in lis:
            a=[]
            for j in range(len(li)):
                if(i==li[j]):
                    a.append(strs[j])
           # print(*a)
            emp.append(a)
        return emp


        

        
        
        
