class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(row: List[str]) -> bool:
            rset = set()
            for r in row:
                if r in rset and r != ".":
                    return False
                rset.add(r)
            return True

        def check_col(col: List[str]) -> bool:
            cset = set()
            for c in col:
                if c in cset and c != ".":
                    return False
                cset.add(c)
            return True

        def check_box(grid: List[List[str]]) -> bool:
            box_set = set()
            for i in range(len(grid)):
                for c in range(len(grid[i])):
                    if grid[i][c] in box_set and grid[i][c]!='.':
                        return False
                    box_set.add(grid[i][c])
            return True

        for i in range(len(board)):
            if not check_row(board[i]):
                return False
            
        for j in range(len(board[0])):
            col = [board[i][j] for i in range(len(board))]
            if not check_col(col):
                return False

        for i in range(0, len(board)-3, 3):
            for j in range(0, len(board[i])-3, 3):
                grid = [row[j:j+3] for row in board[i:i+3]]
                if not check_box(grid):
                    return False
        
        return True