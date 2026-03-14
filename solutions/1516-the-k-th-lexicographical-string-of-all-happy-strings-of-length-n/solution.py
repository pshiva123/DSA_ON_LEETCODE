class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        li=[]
        f(n,1,li,"a")
        f(n,1,li,"b")
        f(n,1,li,"c")
        li.sort()
        print(*li)
        if len(li)<k:
            return ""
        else:
            return li[k-1]



def f(n,idx,li,s):
    if idx==n:
        li.append(s)
        return
    if s[idx-1]=="a":
        f(n,idx+1,li,s+"b")
        f(n,idx+1,li,s+"c")
    if s[idx-1]=="b":
        f(n,idx+1,li,s+"a")
        f(n,idx+1,li,s+"c")
    if s[idx-1]=="c":
        f(n,idx+1,li,s+"b")
        f(n,idx+1,li,s+"a")
        
