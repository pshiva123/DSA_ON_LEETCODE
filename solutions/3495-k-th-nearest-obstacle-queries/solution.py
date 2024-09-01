from sortedcontainers import SortedList
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        obstacles=[]
        temp=SortedList()
        for query in queries:
            s=abs(query[0])+abs(query[1])
            temp.add(s)
            if(len(temp)<k):
                obstacles.append(-1)
            else:
                obstacles.append(temp[k-1])
        return obstacles
