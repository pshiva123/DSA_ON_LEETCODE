from datetime import datetime
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        t1=datetime.strptime(startTime,"%H:%M:%S")
        t2=datetime.strptime(endTime,"%H:%M:%S")
        d=t2-t1
        return int(d.total_seconds())
