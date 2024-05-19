class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        li=[]
        for i in range(len(arr)):
            c=1
            for j in range(len(arr)):
                    if(arr[j]==arr[i]  and i!=j):
                        c+=1
            if(c==1):
                li.append(arr[i])
        m=len(li)
        for i in range(m,k):
            li.append("")
        return li[k-1]    

        
