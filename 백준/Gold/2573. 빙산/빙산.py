import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빙산이 있는 좌표만 저장
icebergs = []
for i in range(n):
    for j in range(m):
        if mapp[i][j] > 0:
            icebergs.append((i,j))

def melt():
    melts = []
    for x, y in icebergs:
        sea = 0
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and mapp[nx][ny] == 0:
                sea += 1
        if sea > 0:
            melts.append((x, y, sea))
    for x, y, sea in melts:
        mapp[x][y] = max(0, mapp[x][y] - sea)

def count_components():
    visited = [[False]*m for _ in range(n)]
    cnt = 0

    for x, y in icebergs:
        if not visited[x][y] and mapp[x][y] > 0:
            cnt += 1
            q = deque()
            q.append((x, y))
            visited[x][y] = True
            while q:
                cx, cy = q.popleft()
                for d in range(4):
                    nx, ny = cx + dx[d], cy + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if mapp[nx][ny] > 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt

year = 0
while True:
    comp = count_components()
    if comp == 0:
        print(0)
        break
    if comp >= 2:
        print(year)
        break
    melt()
    # 빙산 좌표 갱신
    icebergs = [(i, j) for i, j in icebergs if mapp[i][j] > 0]
    year += 1
