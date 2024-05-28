class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        li=[]
        for query in queries:
            #print(query)
            for word in dictionary:
                c=0
                #print(word)
                for k in range(len(query)):
                    if query[k]!=word[k]:
                        c+=1
                    if(c>2):
                        break
                if(c<=2):
                    li.append(query)
                    #print(query,"added")
                    break
        return li

                    

        
