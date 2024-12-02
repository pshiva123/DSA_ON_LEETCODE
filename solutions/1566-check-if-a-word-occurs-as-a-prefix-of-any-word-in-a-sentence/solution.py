class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        li=list(sentence.split())
        for i in range(len(li)):
            if len(li[i])<len(searchWord):
                continue
            if searchWord in li[i][:len(searchWord)]:
                return i+1
        return -1
        
