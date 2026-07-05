class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen = set()
            for j in i:
                if j == '.': continue
                if j in seen: return False
                seen.add(j)
        
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                num = board[j][i]
                if num == '.': continue
                if num in seen: return False
                seen.add(num)
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i+k][j+l]
                        if num == '.': continue
                        if num in seen: return False
                        seen.add(num)
        
        return True