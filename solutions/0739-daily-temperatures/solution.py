class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        n=len(arr)
        idx=n-1
        stack=[[arr[idx],idx]]
        li=[0]
        for i in range(n-2,-1,-1):
            if arr[i]>=stack[-1][0]:
                while stack and arr[i]>=stack[-1][0]:
                    stack.pop()
                if stack:
                    li.append(stack[-1][1]-i)
                else:
                    li.append(0)
                stack.append([arr[i],i])
            else:
                ans=stack[-1][1]-i
                li.append(ans)
                stack.append([arr[i],i])
            #print(*stack)
        li.reverse()
        return li

        
