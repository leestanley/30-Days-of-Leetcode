def check_column_row(board):
    for row in range(9):
        arr_col = []
        arr_row = []
        for column in range(9):
            row_num = board[row][column]
            col_num = board[column][row]
            if row_num != ".":
                if row_num in arr_row:
                    return False
                else:
                    arr_row.append(row_num)
            if col_num != ".":
                if col_num in arr_col:
                    return False
                else:
                    arr_col.append(col_num)
    return True


def check_sub(board):
    for row in range(3):
        for column in range(3):
            arr = []
            for x in range(3):
                for y in range(3):
                    num = board[row * 3 + x][column * 3 + y]
                    if num != ".":
                        if num in arr:
                            return False
                        else:
                            arr.append(num)
    return True


def isValidSudoku(board):
    if check_sub(board) and check_column_row(board):
        return True
    return False


test = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(isValidSudoku(test))
