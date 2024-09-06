class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score)-1):
            max_index=i
            for j in range(i+1,len(score)):
                if score[j][k]>score[max_index][k]:
                    max_index=j
            if(max_index!=i):
                score[i],score[max_index]=score[max_index],score[i]
        return score


        
