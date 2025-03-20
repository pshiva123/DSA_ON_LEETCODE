import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.li=nums
        self.k=k
        self.li.sort()
    def add(self, val: int) -> int:
        bisect.insort(self.li,val)
        return self.li[-(self.k)]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
