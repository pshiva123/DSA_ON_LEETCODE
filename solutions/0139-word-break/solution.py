class TrieNode:
    def __init__(self):
        self.child=[None]*26
        self.flag=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for letter in word:
            idx=ord(letter)-97
            if cur.child[idx] is None:
                cur.child[idx]=TrieNode()
            cur=cur.child[idx]
        cur.flag=True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root=Trie()
        for word in wordDict:
            root.insert(word)
        memo={}
        return back(s,0,root.root,memo)
def back(s,idx,root,memo):
    if idx==len(s):
        return True
    if idx in memo:
        return memo[idx]
    cur=root
    for i in range(idx,len(s)):
        cur_idx=ord(s[i])-97
        if cur.child[cur_idx] is None:
            break
        cur=cur.child[cur_idx]
        if cur.flag:
            if back(s,i+1,root,memo):
                memo[idx]=True
                return True
    memo[idx]=False
    return False
        
    
