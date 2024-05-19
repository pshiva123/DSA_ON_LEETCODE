class Solution:
    def help(self,heights: List[int]) -> int:
        maxi=0
        for i in range(1,len(heights)):
            if(heights[i]>heights[maxi]):
                maxi=i
        return maxi        
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        li=[]
        for i in range(0,len(names)):
            ind=self.help(heights)
            print(ind)
            heights[ind]=0
            li.append(names[ind])
        return li    
                 
                 
