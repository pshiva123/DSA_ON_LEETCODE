class Solution:
    def partitionString(self, s: str) -> int:
        c=0
        set1=set()
        for char in s:
            if char in set1:
                c+=1
                #print(c)
                set1=set()
                set1.add(char)
            else:
                set1.add(char)
            #print(set1)
        return c+1

        
