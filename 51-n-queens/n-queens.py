class Solution:
    def is_safe(self, board: list[list[str]], row: int, col: int, n: int) -> bool:
        for j in range(n):
            if board[row][j] == 'Q':
                return False
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def n_queens(self, ans: list[list[str]], board: list[list[str]], row: int, n: int) -> None:
        if row == n:
            ans.append([''.join(r) for r in board])
            return
        for j in range(n):
            if self.is_safe(board, row, j, n):
                board[row][j] = 'Q'
                self.n_queens(ans, board, row + 1, n)
                board[row][j] = '.'

    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [['.'] * n for _ in range(n)]
        self.n_queens(ans, board, 0, n)
        return ans