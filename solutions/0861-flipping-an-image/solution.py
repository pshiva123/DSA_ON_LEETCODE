class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            for col in range(len(image)):
                image[row][col]=1 if image[row][col]==0 else 0
        li=[]
        for row in range(len(image)):
            l2=[]
            for i in range(len(image)-1,-1,-1):
                l2.append(image[row][i])
            li.append(l2)
        return li
        
