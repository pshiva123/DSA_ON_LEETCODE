import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p,t):
            return (p+1)/(t+1) -p/t
        li=[(-gain(p,t),p,t) for p,t in classes]
        heapq.heapify(li)
        for ex in range(extraStudents):
            g,p,t=heapq.heappop(li)
            p,t=p+1,t+1
            heapq.heappush(li,(-gain(p,t),p,t))
        total=sum(p/t for g,p,t in li)
        return total/len(classes)

        
