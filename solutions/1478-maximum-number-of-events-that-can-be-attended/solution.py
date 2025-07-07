import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by start day
        events.sort(key=lambda e: e[0])
        min_heap = []       # will store end‐times of events that have started
        day = 0
        event_i = 0
        attended = 0
        n = len(events)

        # We only need to sweep up to the latest end day
        last_day = max(e[1] for e in events)

        for day in range(1, last_day + 1):
            # Add all events that start today
            while event_i < n and events[event_i][0] == day:
                heapq.heappush(min_heap, events[event_i][1])
                event_i += 1

            # Remove events that have already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the event that ends the soonest (if any)
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

        return attended

