class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        li=[]
        for i in range(2**len(nums)-1):
            l2=[]
            index=0
            while(i>0):
                if(i&1):
                    l2.append(nums[index])
                index+=1
                i=i>>1
            li.append(l2)
        li.append(nums)
        return li


        
