class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        pairs=0
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                st=words[j][::-1]
                if(words[i]==st):
                    pairs+=1
        return pairs            

        
