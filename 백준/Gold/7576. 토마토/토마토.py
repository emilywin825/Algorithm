import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<m and tomato[xx][yy]==0:
                visited[xx][yy]=visited[x][y]+1
                tomato[xx][yy]=1
                q.append((xx,yy))
    

dx=[1,0,-1,0]
dy=[0,-1,0,1]
m,n=map(int,input().split())
tomato=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
q=deque()
maxx=-987654321000

for i in range(n):
    for j in range(m):
        if tomato[i][j]==1 and visited[i][j]==0:
            q.append((i,j))
            
bfs()

for t in tomato:
    if t.count(0)>0:
        print(-1)
        break
else:
    for v in visited:
        maxx=max(max(v),maxx)
    print(maxx)