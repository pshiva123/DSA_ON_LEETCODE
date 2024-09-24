class Solution:
    def check(self, arr: List[int]) -> bool:
        n=len(arr)
        min_index=0
        for i in range(1,n):
            if arr[i]<arr[min_index]:
                min_index=i
        print(min_index)
        if min_index==0:
            for i in range(n-1,-1,-1):
                if arr[i]<=arr[0]:
                    min_index=i
                else:
                    break
        for i in range(0,n-1):
            print((min_index+i)%n,(min_index+i+1)%n)

            if arr[(min_index+i)%n]>arr[(min_index+i+1)%n]:
                print("enterd")
                return False
        return True

    
        
