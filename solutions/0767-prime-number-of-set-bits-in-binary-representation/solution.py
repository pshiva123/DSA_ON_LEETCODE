class Solution:
    def isPrime(self,num)->bool:
        if num<2:
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c=0
        for num in range(left,right+1):
            st=bin(num)[2:]
            ones=st.count('1')
            #print(ones)
            if self.isPrime(ones):
                c+=1
        return c

        
