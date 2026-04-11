class Solution:
    li=[True]*((10**5)+1)
    li[0]=False
    li[1]=False
    for i in range(2,len(li)):
        if li[i] is True:
            j=i*i
            while j<len(li):
                li[j]=False
                j+=i
    primes=[]
    for i in range(2,len(li)):
        if li[i]:
            primes.append(i)
        
    
    def minOperations(self, nums: list[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            if i%2==0:
                if self.li[nums[i]] is not True:
                    c+=f(self.primes,nums[i])
            else:
                if self.li[nums[i]] is True:
                    if nums[i]==2:
                        c+=2
                    else:
                        c+=1
        return c
def f(primes,ele):
    h=len(primes)-1
    l=0
    idx=-1
    while l<=h:
        m=(l+h)//2
        if primes[m]>ele:
            idx=m
            h=m-1
        else:
            l=m+1
    if idx==-1:
        return 100003-ele
    return primes[idx]-ele
                
                    
        
