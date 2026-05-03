class Solution:
    primes=[True]*(10**3+1)
    primes[0]=False
    primes[1]=False
    for i in range(2,len(primes)):
        if primes[i]:
            j=i*i
            while j<len(primes):
                primes[j]=False
                j+=i
    prefix=[0,0]
    for i in range(2,len(primes)):
        if primes[i]:
            prefix.append(i+prefix[-1])
        else:
            prefix.append(prefix[-1])
        
    def sumOfPrimesInRange(self, n: int) -> int:
        s=str(n)[::-1]
        s=int(s)
        mini=min(s,n)
        maxi=max(s,n)
        if self.primes[mini]:
            return self.prefix[maxi]-self.prefix[mini-1]
        return self.prefix[maxi]-self.prefix[mini]
            
