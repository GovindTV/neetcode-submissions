class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen = set()
            for j in i:
                if j == '.': continue
                if j in seen: return False
                seen.add(j)
        
        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[j][i]
                if num == '.': continue
                if num in seen: return False
                seen.add(num)
        
        for i in [0,3,6]:
            for j in [0,3,6]:
                seen = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i+k][j+l]
                        if num == '.': continue
                        if num in seen: return False
                        seen.add(num)
        
        return True