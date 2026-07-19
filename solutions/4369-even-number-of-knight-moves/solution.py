class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        d=[(-2,-1),(-1,-2),(+1,-2),(+2,-1),(+2,+1),(+1,+2),(-1,+2),(-2,+1)]
        li=[]
        vis=set()
        def check(cur,moves,vis):
            if cur==tuple(target):
                li.append(moves)
                return 
            for x,y in d:
                dx=x+cur[0]
                dy=y+cur[1]
                if (dx,dy) not in vis and 0<=dx<=7 and 0<=dy<=7:
                    vis.add((dx,dy))
                    check((dx,dy),moves+1,vis)
                    # vis.remove((dx,dy))
            return
        vis.add(tuple(start))
        check(tuple(start),0,vis)
        for i in li:
            if i%2==0:
                return True
        return False
            
        
