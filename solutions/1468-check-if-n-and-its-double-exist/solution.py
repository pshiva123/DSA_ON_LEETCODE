class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s=set()
        s.add(arr[0])
        for i in range(1,len(arr)):
            if arr[i]*2 in s or (arr[i]/2) in s:
                return True
            else:
                s.add(arr[i])
        return False

        
