class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        st=""
        for word in words:
            st=st+word[0]
        if(st==s):
            return True
        else:
            return False    

        
