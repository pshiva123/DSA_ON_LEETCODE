class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        li=[]
        temp=[]
        def cs(idx,s):
            if len(li)==k and s==n:
                temp.append(li.copy())
                return
            if len(li)>=k or s>n:
                return
            for i in range(idx,10):
                li.append(i)
                cs(i+1,s+i)
                li.pop()
        cs(1,0)
        return temp
            

                
