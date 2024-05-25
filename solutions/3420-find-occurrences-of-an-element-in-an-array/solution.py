class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        li=[]
        for i in range(len(nums)):
            if(nums[i]==x):
                li.append(i)
        #print(*li)
        li1=[]
        for i in queries:
            if(i>len(li)):
                li1.append(-1)
            else:
                li1.append(li[i-1])
        return li1
                    
        
