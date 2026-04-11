class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer==0:
            return "Green"
        elif 0<timer<30 or timer>90:
            return "Invalid"
        elif timer==30:
            return "Orange"
        return "Red"
        
