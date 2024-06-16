class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        li=[]
        l2=[]
        mini=int(1e9+7)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if(list1[i]==list2[j]):
                    mini=min(mini,(i+j))
                    if(mini==i+j):
                        li.append(list1[i])
                        l2.append((i+j))
        #print(*li,*l2)
        m1=min(l2)
        l3=[]
        for i in range(len(l2)):
            if(l2[i]==m1):
                l3.append(li[i])
        return l3

            

        

        
