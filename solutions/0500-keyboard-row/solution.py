class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l=["qwertyuiop","asdfghjkl","zxcvbnm"]
        l1=[]
        for i in words:
            c1=0
            c2=0
            c3=0
            k= i.lower()
            for j in range(len(i)):
                if k[j] in l[0]:
                    c1+=1
                if k[j] in l[1]:
                    c2+=1
                if k[j] in l[2]:
                    c3+=1
                #print(c1,c2,c3)
            if(c1==len(i) or c2==len(i) or c3==len(i)):
                l1.append(i)
        return l1
        
