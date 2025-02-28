class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def help(s,idx,n,li,ans):
            if idx==n:
                ans.append(li[:])
                return
            for i in range(idx,n):
                if s[idx:i+1]==s[idx:i+1][::-1]:
                    li.append(s[idx:i+1])
                    help(s,i+1,n,li,ans)
                    li.pop()
        ans=[]
        help(s,0,len(s),[],ans)
        return ans
