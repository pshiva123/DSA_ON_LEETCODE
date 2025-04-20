class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score=0
        vis=set()
        i=0
        while(i>=0 and i<len(instructions)):
            if i in vis:
                return score
            else:
                vis.add(i)
            if instructions[i]=="jump":
                i=i+values[i]
            else:
                score+=values[i]
                i+=1
        return score
                    
