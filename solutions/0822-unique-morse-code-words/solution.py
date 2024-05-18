class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
       li=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
       li2=[]
       for word in words:
        st=""
        for i in word:
            k=ord(i)-ord('a')
            st=st+li[k]
        li2.append(st)
       li2=set(li2)
       return len(li2) 
           
            


        
