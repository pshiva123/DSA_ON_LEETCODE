from collections import deque,defaultdict
class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        arr=[1 if i=='1' else -1 for i in s ]
        # total_0=s.count('0')
        # total_1=s.count('1')
        def f(k,maxi):
            x=defaultdict(deque)
            x[0].append(0)
            pref,best=0,0
            for r in range(1,n+1):
                pref+=arr[r-1]
                target=pref-k
                q=x[target]
                lb=r-maxi
                while q and q[0]<lb:
                    q.popleft()
                if q:
                    best=max(best,r-q[0])
                x[pref].append(r)
            return best
        
        
                
       
        ans=f(0,n)
        ans=max(ans,f(-2,2*s.count('1')),f(2,s.count('0')*2))
        return ans
        
            
        
