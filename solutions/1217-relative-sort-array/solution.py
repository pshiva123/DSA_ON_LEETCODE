class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        li=[]
        for i in arr2:
            c=arr1.count(i)
            for j in range(c):
                li.append(i)
        #print(li)
        l2=[]
        for i in arr1:
            if(arr1.count(i)!=li.count(i)):
                l2.append(i)
        l2.sort()
        li+=l2
        return li
        
