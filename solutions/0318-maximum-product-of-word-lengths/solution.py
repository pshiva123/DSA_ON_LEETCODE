class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxi = 0
        l1 = []
        for i in words:
            ex = set(i)
            l1.append(list(ex))
        for i in range(len(l1)):
           # print(*l1[i])
            for j in range(i + 1, len(l1)):
                #print(*l1[j])
                c = 0
                for k in l1[i]:

                    if k in l1[j]:
                        break
                    else:
                        c += 1
                if (c==len(l1[i])):
                    maxi = max(maxi, len(words[i]) * len(words[j]))
                    #print(maxi)
        return maxi

