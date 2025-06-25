class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        sp=image[sr][sc]
        if sp==color:
            return image
        f(image,sr,sc,color,sp)
        return image

    
def f(arr,i,j,color,sp):
    arr[i][j]=color
    n=len(arr)
    m=len(arr[0])
    di=[(-1,0),(1,0),(0,1),(0,-1)]
    for d in di:
        nr,nc=d[0]+i,d[1]+j
        if 0<=nr<n and 0<=nc<m and arr[nr][nc]==sp:
            f(arr,nr,nc,color,sp)

        
