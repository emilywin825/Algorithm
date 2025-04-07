n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]

minn = 987654321

# 모든 8x8 영역 탐색
for h in range(n - 7):
    for w in range(m - 7):
        new_chess = [row[w:w+8] for row in chess[h:h+8]]
        count_w_start = 0  # 시작이 W일 때 칠할 칸 수
        count_b_start = 0  # 시작이 B일 때 칠할 칸 수

        for i in range(8):
            for j in range(8):
                expected_color_w = 'W' if (i + j) % 2 == 0 else 'B'
                expected_color_b = 'B' if (i + j) % 2 == 0 else 'W'

                if new_chess[i][j] != expected_color_w:
                    count_w_start += 1
                if new_chess[i][j] != expected_color_b:
                    count_b_start += 1

        minn = min(minn, count_w_start, count_b_start)

print(minn)
