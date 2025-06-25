from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue=deque([])
        queue.append((beginWord,1))
        s=set(wordList)
        while queue:
            word=queue.popleft()
            if word[0]==endWord:
                return word[1]
            for i in range(len(word[0])):
                for j in range(26):
                    x=word[0][:i]+chr(97+j)+word[0][i+1:]
                    if x in s:
                        queue.append((x,word[1]+1))
                        s.remove(x)
        return 0
        
