class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        ans=""
        for i in sorted_d:
            ans+=i*sorted_d[i]
        return ans
