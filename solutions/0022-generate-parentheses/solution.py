class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def help(n,st,obc,cbc,li):
            if len(st)==n:
                li.append(st)
                return
            if obc<(n//2):
                help(n,st+'(',obc+1,cbc,li)
            if cbc<obc:
                help(n,st+')',obc,cbc+1,li)
        li=[]
        help(2*n,"",0,0,li)
        return li

        
