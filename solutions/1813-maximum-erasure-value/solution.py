class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i=0
        j=0
        n=len(nums)
        maxi=-1
        s=set()
        while(i<n and j<n):
            if nums[i] not in s:
                s.add(nums[i])
                maxi=max(maxi,sum(s))
            else:
                maxi=max(maxi,sum(s))
                temp=0
                for x in range(j,i):
                    temp+=1
                    if nums[x]==nums[i]:
                        s.remove(nums[x])
                        s.add(nums[i])
                        break
                    else:
                        s.remove(nums[x])
                j=j+temp
                #print(j,s)
            i+=1
        return maxi
            






        
