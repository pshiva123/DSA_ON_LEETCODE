class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        set1=('a','c','e','g')
        set2=('b','d','f','h')
        color1=0
        color2=0
        if coordinate1[0] in set1:
            if(int(coordinate1[1])%2==0):
                color1=0
            else:
                color1=1
        else:
            if(int(coordinate1[1])%2==0):
                color1=1
            else:
                color1=0
        if coordinate2[0] in set1:
            if(int(coordinate2[1])%2==0):
                color2=0
            else:
                color2=1
        else:
            if(int(coordinate2[1])%2==0):
                color2=1
            else:
                color2=0
        print(color1,color2)
        if(color1==color2):
            return True
        return False




        
