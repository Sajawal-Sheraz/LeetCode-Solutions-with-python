def isValidSudoku(board) -> bool:
    end = 3
    start = 0
    result = []
    for col in range(3):
        count = 0
        temp_board = []
        for i in range(9):
            if count > 2:
                count = 0
                result.append(solve(temp_board))
                temp_board = []
            temp_board.append(board[i][start:end])
            count += 1
        result.append(solve(temp_board))
        start = start + 3
        end = end + 3
    res = set(result)
    if len(res) > 1 or list(res)[0] == False:
        return False
    elif list(res)[0] == True:
        have to do it
        return True


def solve(board):
    validator = {}
    for i in range(3):
        for j in range(3):
            if validator.get(board[i][j], None) is not None and board[i][j] != ".":
                return False
            if board[i][j] == ".":
                continue
            validator[board[i][j]] = board[i][j]
    if len(validator) < 1:
        return False
    return True


[
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]


[
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]
one_board = [
    ["8", ".", "."],
    ["4", ".", "."],
    ["7", ".", "."],
]


print(isValidSudoku(board))
