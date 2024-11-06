class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={}
        dic[0]=1
        pre=0
        count=0
        for i in range(len(nums)):
            pre+=nums[i]
            temp=pre-k
            if temp in dic:
                count+=dic[temp]
            if pre in dic:
                dic[pre]+=1
            else:
                dic[pre]=1
        return count


         

        
