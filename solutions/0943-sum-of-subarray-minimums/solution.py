class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        nextsmaller=findnextsmaller(arr,n)
        prevsmaller=findprevsmaller(arr,n)
        ans=0
        for i in range(n):
            lefty=i-prevsmaller[i]
            right=nextsmaller[i]-i
            ans=(ans+(lefty*right)*arr[i])%int(1e9+7)
        return ans




def findnextsmaller(arr,n):
    nextsmaller=[n]*n #to store indices
    li=[n-1]
    for i in range(n-2,-1,-1):
        while li and arr[i]<=arr[li[-1]]:
            li.pop()
        if li:
            nextsmaller[i]=li[-1]
        li.append(i)
    return nextsmaller

def findprevsmaller(arr,n):
    prevsmaller=[-1]*n
    li=[0]
    for i in range(1,n):
        while li and arr[i]<arr[li[-1]]:
            li.pop()
        if li:
            prevsmaller[i]=li[-1]
        li.append(i)
    return prevsmaller

