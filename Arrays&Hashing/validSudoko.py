def validSudoku(board):
    seen = set()
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != ".":
                row_key = f"row{i}-{num}"
                col_key = f"col{j}-{num}"
                box_key = f"box{i//3}{j//3}-{num}"
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
    
    return True

board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
]

print(validSudoku(board))  # True

#0073DBCF

#8F1560