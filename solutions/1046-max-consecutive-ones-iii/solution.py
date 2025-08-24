class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j,n=0,0,len(nums)
        flip=0
        ans=0
        while(i<n and j<n):
            if nums[i]==1:
                i+=1
            else:
                if flip<k:
                    flip+=1
                else:
                    ans=max(ans,(i-1)-j+1)
                    while flip>=k and j<n:
                        if nums[j]==0:
                            flip-=1
                        j+=1
                    flip+=1
                i+=1
        return max(ans,(i-1)-j+1)



        
