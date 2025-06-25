class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        queue=deque([])
        queue.append((beginWord,1))
        s=set(wordList)
        cnt=0
        di={}
        di[beginWord]=1
        if beginWord in s:
            s.remove(beginWord)
        while queue:
            word=queue.popleft()
            if word[0]==endWord:
                cnt=word[1]
                di[word[0]]=cnt
                break
            for i in range(len(word[0])):
                for j in range(26):
                    x=word[0][:i]+chr(97+j)+word[0][i+1:]
                    if x in s:
                        queue.append((x,word[1]+1))
                        di[x]=word[1]+1
                        s.remove(x)
        if cnt==0:
            return []
        else:
            ans=[]
            #print(di)
            dfs(di,beginWord,endWord,[endWord],ans)
            for i in range(len(ans)):
                ans[i]=ans[i][::-1]
            return ans


def dfs(di,beginWord,last,li,ans):
    if last==beginWord:
        #print(li)
        ans.append(li)
        return 
    temp=last
    for i in range(len(temp)):
        for j in range(26):
            x=temp[:i]+chr(97+j)+temp[i+1:]
            if x in di and di[x]<di[temp]:
                dfs(di,beginWord,x,li+[x],ans)

        
        
