import math
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        li=[]
        for i in range(len(boxes)):
            su=0
            for j in range(len(boxes)):
                if(i==j):
                    continue
                if(boxes[j]=="1"):
                    su += (abs(i-j))
            li.append(su)
        return li        

        
