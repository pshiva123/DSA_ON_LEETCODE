class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=""
        lngst=""
        i=0
        while(i<len(s)):
            if s[i] not in st:
                st=st+s[i]
                #print(st)
            else:
                #print("entered into else")
                if(len(st)>len(lngst)):
                    lngst=st
                m=st.index(s[i])
                st=st[m+1:]
                st=st+s[i]
                #print(st)
            i+=1
        if(len(st)>len(lngst)):
            lngst=st
        return len(lngst)



        
