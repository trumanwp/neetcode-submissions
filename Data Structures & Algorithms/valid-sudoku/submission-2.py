class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # define defaultdicts, to store values for each row,col and square
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # Loop through rows + cols
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": 
                    continue
                if (board[r][c] in cols[c] or
                    board[r][c] in rows[r] or
                    board[r][c] in squares[(r//3, c//3)]): # square are held as coordinates up to (2,2), so we can divide r,c by 3
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])    

        return True           

