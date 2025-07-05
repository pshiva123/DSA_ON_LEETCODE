class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0],x[1]))
        n=len(intervals)
        li=[]
        print(intervals)
        first=intervals[0][0]
        last=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<=last and intervals[i][1]<=last:
                continue
            if intervals[i][0]<=last:
                #li.append(intervals[i])
                last=intervals[i][1]
            else:
                print(first,last)
                li.append([first,last])
                first=intervals[i][0]
                last=intervals[i][1]
        if li and li[-1]!=[first,last]:
            li.append([first,last])
        if not li:
            li.append([first,last])
        return li

        
