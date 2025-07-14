class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n=len(s1)
        if n<len(s2) or Counter(s1)!=Counter(s2):
            return False
        return dfs(s1,s2,0, 0, n,{})



def dfs(s1,s2,i1: int, i2: int, length: int,d) -> bool:
    sub1 = s1[i1:i1+length]
    sub2 = s2[i2:i2+length]
    if sub1 == sub2:
        return True
    if (i1,i2,length) in d:
        return d[(i1,i2,length)]

    for l in range(1, length):
        x= dfs(s1,s2,i1, i2, l,d) and dfs(s1,s2,i1+l, i2+l, length-l,d)
        y=dfs(s1,s2,i1, i2+length-l, l,d) and dfs(s1,s2,i1+l, i2, length-l,d)
        d[(i1,i2,length)]= x or y
        if x or y:
            return True
    d[(i1,i2,length)]=False
    return False
        

            

       
        
