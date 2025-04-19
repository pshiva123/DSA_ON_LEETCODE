from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c=Counter(s)
        sorted_keys=[i for i in c]
        sorted_keys.sort()
        sorted_items=[]
        for i in sorted_keys:
            sorted_items.append([i,c[i]])
        print(sorted_items)
        li=['']*len(s)
        last=len(s)-1
        first=0
        repated_odd=""
        for i in sorted_items:
            flag=True
            cnt=i[1]
            if i[1]%2==1:
                repated_odd=i[0]
                cnt-=1
            while cnt>0:
                if flag:
                    li[first]=i[0]
                    first+=1
                else:
                    li[last]=i[0]
                    last-=1
                cnt-=1
                flag= not flag
        if repated_odd!="":
            li[first]=repated_odd
        return ''.join(li)
