class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        idx=-1
        n=len(capacity)
        for i in range(n):
            if capacity[i]>=itemSize:
                if idx==-1:
                    idx=i
                else:
                    if capacity[i]<capacity[idx]:
                        idx=i
        return idx
        
