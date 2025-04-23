class Solution:
    def countLargestGroup(self, n: int) -> int:
        di={}
        for i in range(1,n+1):
            ss=0
            while i>0:
                ss+=i%10
                i=i//10
            if ss in di:
                di[ss].append(i)
            else:
                li=[i]
                di[ss]=li
        largest=1
        for s in di:
            if len(di[s])>largest:
                largest=len(di[s])
        cnt=0
        for s in di:
            if len(di[s])==largest:
                cnt+=1
        return cnt
        
