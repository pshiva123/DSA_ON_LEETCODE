class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        if s[0]=="]" or s[0]=="}" or s[0]=="]":
            return False
        li.append(s[0])
        for i in range(1,len(s)):
            if s[i]=="{" or s[i]=="(" or s[i]=="[":
                li.append(s[i])
            elif s[i]=="}":
                if(len(li)==0):
                    return False
                if(li[-1]=="{"):
                    li.pop()
                else:
                    li.append(s[i])
            elif s[i]=="]":
                if(len(li)==0):
                    return False
                if(li[-1]=="["):
                    li.pop()
                else:
                    li.append(s[i])
            elif s[i]==")":
                if(len(li)==0):
                    return False
                if(li[-1]=="("):
                    li.pop()
                else:
                    li.append(s[i])
        if(len(li)==0):
            return True
        return False
            
            

           
        
