class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt=0
        n=len(strs)
        cols=set()
        for i in range(n-1):
            for j in range(len(strs[i])):
                if strs[i][j]>strs[i+1][j]:
                    if j not in cols:
                        cols.add(j)
        return len(cols)


