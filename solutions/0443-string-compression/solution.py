class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        n=len(chars)
        li=[]
        cnt=1
        for i in range(1,n):
            if chars[i]==chars[i-1]:
                cnt+=1
            else:
                li.append([chars[i-1],cnt])
                cnt=1

        li.append([chars[-1],cnt])
        idx=0
        print(li)
        for i in li:
            chars[idx]=i[0]
            idx+=1
            m=i[1]
            if m==1:
                continue
            temp=[]
            while m>0:
                temp.append(m%10)
                m=m//10
            temp=temp[::-1]
            for j in temp:
                chars[idx]=str(j)
                idx+=1
       
        return idx

   

        
