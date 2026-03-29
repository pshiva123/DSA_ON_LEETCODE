import heapq
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.li=[]
        self.cur={}
        for eve in events:
            self.cur[eve[0]]=eve[1]
            heapq.heappush(self.li,(-eve[1],eve[0]))
        

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.cur[eventId]=newPriority
        heapq.heappush(self.li,(-newPriority,eventId))

  

    def pollHighest(self) -> int:
        while self.li:
            negp,eveId=self.li[0]
            if self.cur.get(eveId)==-negp:
                del self.cur[eveId]
                heapq.heappop(self.li)
                return eveId
            heapq.heappop(self.li)
        return -1
        
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
