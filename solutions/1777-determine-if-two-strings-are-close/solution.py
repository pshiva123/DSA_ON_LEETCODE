class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dit1={}
        dit2={}
        for i in range(len(word1)):
            if word1[i] in dit1:
                dit1[word1[i]]+=1
            else:
                dit1[word1[i]]=1
        for i in range(len(word2)):
            if word2[i] in dit2:
                dit2[word2[i]]+=1
            else:
                dit2[word2[i]]=1
        s1=list(dit1.values())
        s2=list(dit2.values())
        ans1=set(dit1.keys())
        ans2=set(dit2.keys())
        s1.sort()
        s2.sort()
        return s1==s2 and ans1==ans2

