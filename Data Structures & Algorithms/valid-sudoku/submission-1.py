class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_group(group):
            filtered=[i for i in group if i!='.']
            return len(filtered)==len(set(filtered))
        for row in board:
            if not is_valid_group(row):
                return False
        for col_index in range(9):
            column=[row[col_index] for row in board]
            if not is_valid_group(column):
                return False
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                box=[]
                for r in range(box_row,box_row+3):
                    for c in range(box_col,box_col+3):
                        box.append(board[r][c])
                if not is_valid_group(box):
                    return False
        return True