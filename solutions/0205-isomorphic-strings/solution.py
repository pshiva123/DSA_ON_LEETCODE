from collections import OrderedDict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        se=set()
        for i in range(len(s)):
            if t[i] in dic:
                if dic[t[i]]!=s[i]:
                    return False
            else:
                if s[i] in se:
                    return False
                dic[t[i]]=s[i]
            se.add(s[i])
        return True

        
