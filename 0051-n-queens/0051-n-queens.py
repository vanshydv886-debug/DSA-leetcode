class Solution:
    def solve(self, col, board, ans, leftRow, upperDiagonal, lowerDiagonal, n):
        if col == n:
            ans.append(board[:])
            return

        for row in range(n):
            if (
                leftRow[row] == 0
                and lowerDiagonal[row + col] == 0
                and upperDiagonal[n - 1 + col - row] == 0
            ):
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                leftRow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1

                self.solve(
                    col + 1,
                    board,
                    ans,
                    leftRow,
                    upperDiagonal,
                    lowerDiagonal,
                    n,
                )

                board[row] = board[row][:col] + "." + board[row][col + 1:]
                leftRow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n):
        ans = []
        board = ["." * n for _ in range(n)]

        leftRow = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)

        self.solve(
            0,
            board,
            ans,
            leftRow,
            upperDiagonal,
            lowerDiagonal,
            n,
        )

        return ans
        