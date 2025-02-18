# 최단거리 찾기 : bfs
# 출발점에서 도착점까지 이동한 최소 횟수를 출력
# 출발점은 (1,1) / 도착점은 (7,7)
# 1 : 격자판, 0 : 도로
# dis : 거리

from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
maze=[list(map(int,input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
Q=deque()
# ch=set()
Q.append((0,0))
maze[0][0]=1
# ch.add((0,0))

while Q:
    node=Q.popleft()
    for j in range(4):
        x=node[0]+dx[j]
        y=node[1]+dy[j]
        if 0<=x<=6 and 0<=y<=6 and maze[x][y]==0:
            maze[x][y]=1
            dis[x][y]=dis[node[0]][node[1]]+1
            Q.append((x,y))

if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])

# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 0