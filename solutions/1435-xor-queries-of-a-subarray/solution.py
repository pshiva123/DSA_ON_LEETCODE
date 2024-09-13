class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor=[0]*len(arr)
        li=[]
        xor[0]=arr[0]
        for i in range(1,len(arr)):
            xor[i]=arr[i]^xor[i-1]
        for query in queries:
            if query[0]==0:
                li.append(xor[query[1]])
            else:
                li.append(xor[query[1]]^xor[query[0]-1])        
        return li
