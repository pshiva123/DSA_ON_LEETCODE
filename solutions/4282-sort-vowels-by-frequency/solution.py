class Solution:
    def sortVowels(self, s: str) -> str:
        ans=""
        d={}
        n=len(s)
        vowels=set('aeiou')
        for i in range(n):
            if s[i] in vowels:
                if s[i] in d:
                    d[s[i]][1]+=1
                else:
                    d[s[i]]=[i,1]
        li=[]
        for key in d:
            li.append([key,d[key][0],d[key][1]])
        li.sort(key=lambda x:(-x[2],x[1]))
        idx=0
        for i in range(n):
            if s[i] not in vowels:
                ans+=s[i]
            else:
                if li[idx][2]<=0:
                    idx+=1
                ans+=li[idx][0]
                li[idx][2]-=1
        return ans
        
                    
                
        
