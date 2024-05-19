class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start=[]
        end=[]
        for li in paths:
            start.append(li[0])
            end.append(li[1])
        for place in start:
            if(end.count(place)>0):
                end.remove(place)
        return end[0]            
        
