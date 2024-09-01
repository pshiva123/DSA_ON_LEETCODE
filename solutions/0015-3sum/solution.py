class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ret=[]
        for i in range(n-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            s=0-nums[i]
            j=i+1
            k=n-1
            while(j<k):
                tempsum=nums[j]+nums[k]
                if(tempsum==s):
                    ret.append([nums[i],nums[j],nums[k]])
                    while(j<k and nums[j]==nums[j+1]):
                        j+=1
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1
                    j+=1
                    k-=1
                elif(tempsum>s):
                    k-=1
                else:
                    j+=1
        return ret


        
