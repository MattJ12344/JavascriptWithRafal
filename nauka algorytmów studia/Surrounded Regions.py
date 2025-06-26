from typing import List, Tuple
from collections import deque

class Solution(object):
    def solve(self, board: List[List[str]]) -> None:
        """
        :type board: List[List[str]]
        :rtype: None
        """
        if not board or not board[0]:
            return

        num_rows: int = len(board)
        num_cols: int = len(board[0])
        queue: deque[Tuple[int, int]] = deque()

        for row in range(num_rows):
            if board[row][0] == "O":
                queue.append((row, 0))
            if board[row][num_cols - 1] == "O":
                queue.append((row, num_cols - 1))

        for col in range(num_cols):
            if board[0][col] == "O":
                queue.append((0, col))
            if board[num_rows - 1][col] == "O":
                queue.append((num_rows - 1, col))

        def in_bounds(row: int, col: int) -> bool:
            return (0 <= row < num_rows) and (0 <= col < num_cols)

        while queue:
            row, col = queue.popleft()
            board[row][col] = "#"

            for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + d_row, col + d_col
                if not in_bounds(new_row, new_col):
                    continue
                if board[new_row][new_col] != "O":
                    continue
                queue.append((new_row, new_col))
                board[new_row][new_col] = "#"

        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"
                    

# Test 1               
board1 = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
Solution().solve(board1)
assert board1 == [
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "O", "X", "X"]
]

# Test 2
board2 = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]
Solution().solve(board2)
assert board2 == [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]

# Test 3
board3 = [["X"]]
Solution().solve(board3)
assert board3 == [["X"]]

# Test 4
board4 = [["O"]]
Solution().solve(board4)
assert board4 == [["O"]]

# Test 5
board5 = [
    ["X", "O", "X", "X"],
    ["O", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
Solution().solve(board5)
assert board5 == [
    ["X", "O", "X", "X"],
    ["O", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]

# Test 6
board6 = [["X", "O", "X"]]
Solution().solve(board6)
assert board6 == [["X", "O", "X"]]

print("ktos")