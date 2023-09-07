# Improved version of the Sudoku solver code with added comments in Korean

from tkinter import Tk, Entry, Button, Label

# 주어진 위치에 숫자를 놓을 수 있는지 검사하는 함수
def is_valid_move(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

# 스도쿠 보드를 해결하는 함수
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

# 빈 셀의 위치를 찾는 함수
def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Tkinter 창을 초기화하는 부분
root = Tk()
root.title("Sudoku Solver")

# 9x9 그리드로 구성된 Entry 위젯 생성
entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        e = Entry(root, width=2, font=("Arial", 24), justify="center")
        e.grid(row=i, column=j)
        row_entries.append(e)
    entries.append(row_entries)

# UI로부터 보드 상태를 읽어오는 함수
def read_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            # 입력값 유효성 검사
            if val:
                try:
                    row.append(int(val))
                except ValueError:
                    row.append(0)
            else:
                row.append(0)
        board.append(row)
    return board

# 해결된 보드 상태를 UI에 업데이트하는 함수
def update_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, "end")
            entries[i][j].insert(0, str(board[i][j]))

# UI 보드를 리셋하는 함수
def reset_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, "end")
            entries[i][j].config(fg="black")

# 스도쿠 퍼즐을 해결하는 함수
def solve():
    board = read_board()
    if solve_sudoku(board):
        update_board(board)

# 'Go' 버튼 생성
go_button = Button(root, text="Go", command=solve)
go_button.grid(row=9, column=0, columnspan=4)

# 'Reset' 버튼 생성
reset_button = Button(root, text="Reset", command=reset_board)
reset_button.grid(row=9, column=5, columnspan=4)

# Tkinter 이벤트 루프 시작
root.mainloop()
