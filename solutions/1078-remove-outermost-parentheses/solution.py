class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ret=""
        stack=[]
        for i in s:
            if i=="(":
                if len(stack)>0:
                    ret+="("
                stack.append(i)

            else:
                stack.pop()
                if stack:
                    ret+=")"
        return ret
                    


