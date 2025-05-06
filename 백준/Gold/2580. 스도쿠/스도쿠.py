import sys
input = sys.stdin.readline

# 스도쿠 판 입력
board = [list(map(int, input().split())) for _ in range(9)]

# 빈칸 위치 수집
blank = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

# 행, 열, 3x3 사각형에 사용된 숫자 저장
row_used = [set() for _ in range(9)]
col_used = [set() for _ in range(9)]
square_used = [set() for _ in range(9)]

# 초기 사용 숫자 등록
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num != 0:
            row_used[i].add(num)
            col_used[j].add(num)
            square_used[(i // 3) * 3 + (j // 3)].add(num)

# 백트래킹 함수
def solve(depth):
    if depth == len(blank):
        for row in board:
            print(*row)
        return True  # 정답 찾았으므로 종료

    x, y = blank[depth]
    square_idx = (x // 3) * 3 + (y // 3)

    for num in range(1, 10):
        if (num not in row_used[x] and
            num not in col_used[y] and
            num not in square_used[square_idx]):

            board[x][y] = num
            row_used[x].add(num)
            col_used[y].add(num)
            square_used[square_idx].add(num)

            if solve(depth + 1):
                return True  # 정답 찾았으므로 바로 종료

            # 백트래킹
            board[x][y] = 0
            row_used[x].remove(num)
            col_used[y].remove(num)
            square_used[square_idx].remove(num)

    return False  # 가능한 숫자 없음 → 백트래킹

solve(0)