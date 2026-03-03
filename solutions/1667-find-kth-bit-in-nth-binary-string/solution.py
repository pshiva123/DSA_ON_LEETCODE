class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(2,n+1):
            s=s+"1"+reverse(invert(s))
        print(s)
        return s[k-1]
def reverse(s):
    s=s[::-1]
    return s
def invert(s):
    new_s=""
    for i in s:
        if i=="1":
            new_s+="0"
        else:
            new_s+="1"
    return new_s        
