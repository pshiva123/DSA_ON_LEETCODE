class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        st1=""
        st2=""
        for s in word1:
            st1+=s
        for s in word2:
            st2+=s
        li1=[]
        li2=[]
        for i in st1:
            li1.append(i)
        for i in st2:
            li2.append(i)
       # li1=li1.sort()
       # li2=li2.sort()
        if(li1==li2):
            return True
        else:
            return False    

        
