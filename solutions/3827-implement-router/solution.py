from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List, Tuple

class Router:
    def __init__(self, memoryLimit: int):
        self.ml = memoryLimit
        self.queue: deque[Tuple[int,int,int]] = deque()     
        self.packet_set: set[Tuple[int,int,int]] = set()   
        self.dest_map: dict[int, List[int]] = defaultdict(list)
        self.dest_start: dict[int, int] = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        p = (source, destination, timestamp)
        
        if p in self.packet_set:
            return False

    
        if len(self.queue) == self.ml:
            old = self.queue.popleft()
            self.packet_set.remove(old)
            d_old = old[1]
           
            self.dest_start[d_old] += 1
            
            if self.dest_start[d_old] == len(self.dest_map[d_old]):
                del self.dest_map[d_old]
                del self.dest_start[d_old]

       
        self.queue.append(p)
        self.packet_set.add(p)
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        p = self.queue.popleft()
        self.packet_set.remove(p)

        
        d = p[1]
        self.dest_start[d] += 1
        if self.dest_start[d] == len(self.dest_map[d]):
            del self.dest_map[d]
            del self.dest_start[d]

        return [p[0], p[1], p[2]]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0

        timestamps = self.dest_map[destination]
        start_idx = self.dest_start[destination]

        
        lo = bisect_left(timestamps, startTime, start_idx)
        hi = bisect_right(timestamps, endTime, start_idx)
        return hi - lo

