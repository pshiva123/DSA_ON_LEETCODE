class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        ans=0
        for i in s:
            if i=="(":
                st.append(i)
            elif i==")":
                ans=max(ans,len(st))
                if len(st)>0:
                    st.pop()
        return ans

        
