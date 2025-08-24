class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        ss=set('{[(')
        for ch in s:
            if ch in ss:
                li.append(ch)
            else:
                if len(li)==0:
                    print(11)
                if (ch=='}' and li and li[-1]=='{') or(
                    ch==']' and li and li[-1]=='[') or(
                    ch==')' and li and li[-1]=='('):
                    li.pop()
                else:
                    return False
        return len(li)==0
        
