class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        longest=events[0][1]
        idx=events[0][0]
        for i in range(1,len(events)):
            temp=events[i][1]-events[i-1][1]
            if temp>longest:
                longest=temp
                idx=events[i][0]
            elif temp==longest:
                idx=min(events[i][0],idx)
        return idx
