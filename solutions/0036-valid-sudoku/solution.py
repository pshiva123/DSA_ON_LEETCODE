class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        subgrids=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=board[i][j]
                    if (num in rows[i]) or (num in cols[j]) or (num in subgrids[(i//3)*3+(j//3)]):
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    subgrids[(i//3)*3+(j//3)].add(num)
        return True

        
