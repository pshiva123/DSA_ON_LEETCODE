class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = {}
        for i in t:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1

        left = 0
        right = 0
        n = len(s)
        d2 = {}
        ans = ""

        while right < n:   # fixed
            d2[s[right]] = d2.get(s[right], 0) + 1   # simplified

            while valid(d1, d2):
                if ans == "" or len(ans) > (right - left + 1):   # fixed
                    ans = s[left:right+1]

                d2[s[left]] -= 1
                if d2[s[left]] == 0:
                    d2.pop(s[left])

                left += 1

            right += 1

        return ans


def valid(d1, d2):
    for val in d1:
        if val not in d2 or d1[val] > d2[val]:
            return False
    return True
