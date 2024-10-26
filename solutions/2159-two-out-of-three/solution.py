class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        s3=set(nums3)
        sa1=s1&s2
        sa2=s1&s3
        sa3=s2&s3
        li=[]
        li.extend(sa1)
        li.extend(sa2)
        li.extend(sa3)
        li=list(set(li))
        return li        
