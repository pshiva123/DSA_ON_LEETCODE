import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        flag=True
        a,b,c=sides[0],sides[1],sides[2]
        if (sides[0]>=sides[1]+sides[2]) or (sides[1]>=sides[0]+sides[2]) or (sides[2]>=sides[1]+sides[0]):
            return []
        A=math.degrees(math.acos((b*b+c*c-a*a)/(2*b*c)))
        B=math.degrees(math.acos((a*a+c*c-b*b)/(2*a*c)))
        C=math.degrees(math.acos((a*a+b*b-c*c)/(2*b*a)))
        li=[A,B,C]
        li.sort()
        return li
        
