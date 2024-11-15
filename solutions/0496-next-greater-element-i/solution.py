class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        li=[]
        for i in range(len(nums2)):
            d[nums2[i]]=i
        print(d)
        for i in nums1:
            idx=d[i]
            ele=-1
            for j in range(idx,len(nums2)):
                if nums2[j]>i:
                    ele=nums2[j]
                    break
            li.append(ele)
        return li




        
