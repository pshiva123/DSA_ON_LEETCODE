class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n=len(code)
        li=[]
        check=["electronics","grocery","pharmacy","restaurant"]
        priority={cat:i for i,cat in enumerate(check)}
        for i in range(n):
            if code[i]=="":
                continue
            if isActive[i]==True and businessLine[i] in check:
                flag=True
                for j in code[i]:
                    x=ord(j)
                    if 97<=x<=122 or 65<=x<=90 or 48<=x<=57 or x==95:
                        continue
                    else:
                        flag=False
                if flag:
                    li.append([code[i],businessLine[i]])
        li.sort(key=lambda item:(priority.get(item[1],float('inf')),item[0]))
        #print(li)
    
        return [i[0] for i in li]
                        
                
        
