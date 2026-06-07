class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        li=[]
        def build(st,pos,curcost):
            if curcost>k:
                return 
            if pos==n:
                li.append(st)
                return 
            if st and st[-1]=="1":
                build(st+"0",pos+1,curcost)
            else:
                build(st+"1",pos+1,curcost+pos)
                build(st+"0",pos+1,curcost)
        build("",0,0)
        return li
        
