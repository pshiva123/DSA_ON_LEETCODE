class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        li=[]
        n=len(words)
        for i in range(n-1):
            a=words[i]
            b=words[i+1]
            idx=0
            while idx<min(len(a),len(b)) and a[idx]==b[idx]:
                idx+=1
            li.append(idx)
        prevmax=[0]*(n-1)
        nextmax=[0]*(n-1)
        cur=0
        for i in range(n-1):
            cur=max(cur,li[i])
            prevmax[i]=cur
        cur=0
        for i in range(n-2,-1,-1):
            cur=max(cur,li[i])
            nextmax[i]=cur
        ans=[0]*n
        for i in range(n):
            idx=0
            if 0<i<n-1:
                a=words[i-1]
                b=words[i+1]
                while idx<min(len(a),len(b)) and a[idx]==b[idx]:
                    idx+=1
            left=prevmax[i-2] if i-2>=0 else 0
            right=nextmax[i+1] if i+1<n-1 else 0
            ans[i]=(max(left,right,idx))
        return ans
            
            
            
            
                
        
