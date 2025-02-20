class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table={}
        table[2]=["a","b","c"]
        table[3]=["d","e","f"]
        table[4]=["g","h","i"]
        table[5]=["j","k","l"]
        table[6]=["m","n","o"]
        table[7]=["p","q","r","s"]
        table[8]=["t","u","v"]
        table[9]=["w","x","y","z"]
        # now logic start
        temp=[]
        li=""
        def  help(idx,li):
            if idx==len(digits):
                temp.append(li) 
                return
            
            value=table[int(digits[idx])]
            for j in value:
                li+=j
                help(idx+1,li)
                li=li[:-1]
                

        help(0,li)
        if temp[0]=="":
            return []
        return temp




    
    
        
