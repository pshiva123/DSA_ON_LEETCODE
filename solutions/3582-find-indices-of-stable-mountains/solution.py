class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        li=[]
        for i in range(1,len(height)):
            if(height[i-1]>threshold):
                li.append(i)
        return li
        
