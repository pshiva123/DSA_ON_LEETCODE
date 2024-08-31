class Solution:
    def stringHash(self, s: str, k: int) -> str:
        li=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        i=0
        retst=""
        while(i<len(s)):
            st=s[i:i+k]
            #print(st)
            hashsum=0
            for j in range(len(st)):
                m=ord(st[j])
                m=m-97
                hashsum+=m
                #print(hashsum)
            hashsum%=26
            hashsum+=97
            retst+=chr(hashsum)
            i+=k
        return retst





        
        
