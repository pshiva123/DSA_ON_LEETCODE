from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        self.solver(num, "", 0, 0, 0, target, ans)
        return ans

    def solver(self, num, expr, idx, eval_val, prev_num, target, ans):
        if idx == len(num):
            if eval_val == target:
                ans.append(expr)
            return

        for i in range(idx, len(num)):
            if num[idx] == "0" and i > idx:  # Prevent numbers like "05"
                break
            curr_num = int(num[idx:i+1])  # Convert substring to integer
            
            if idx == 0:
                self.solver(num, expr + str(curr_num), i + 1, curr_num, curr_num, target, ans)
            else:
                self.solver(num, expr + "+" + str(curr_num), i + 1, eval_val + curr_num, curr_num, target, ans)
                self.solver(num, expr + "-" + str(curr_num), i + 1, eval_val - curr_num, -curr_num, target, ans)
                self.solver(num, expr + "*" + str(curr_num), i + 1, eval_val - prev_num + prev_num * curr_num, prev_num * curr_num, target, ans)

