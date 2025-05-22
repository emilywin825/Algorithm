import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    dx=[-1,0,1,0,0,0]
    dy=[0,1,0,-1,0,0]
    dh=[0,0,0,0,1,-1]
    while q:
        z,x,y=q.popleft()
        for i in range(6):
            xx=x+dx[i]
            yy=y+dy[i]
            zz=z+dh[i]
            if 0<=xx<n and 0<=yy<m and 0<=zz<h and visited[zz][xx][yy]==0 and tomato[zz][xx][yy]==0:
                    q.append((zz,xx,yy))
                    visited[zz][xx][yy]=visited[z][x][y]+1
                    tomato[zz][xx][yy]=1
                    
m,n,h=map(int,input().split())
tomato=[[list(map(int,input().split())) for _ in range(n)]for _ in range(h)]
visited=[[[0]*m for _ in range(n)] for _ in range(h)]
q=deque()

for i in range(h):
     for j in range(n):
          for k in range(m):
               if tomato[i][j][k]==1 and visited[i][j][k]==0:
                    q.append((i,j,k))

bfs()

maxx=-987654321000
for tt in tomato:
    for t in tt:
        if 0 in t:
            print(-1)
            exit(0)
else:
    for vv in visited:
        for v in vv:
            maxx=max(maxx,max(v))
    print(maxx)