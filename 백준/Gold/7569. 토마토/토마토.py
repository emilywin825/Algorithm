from collections import deque
import sys
input=sys.stdin.readline
#위,아래,왼,오,앞,뒤
dx=[0,0,-1,0,1,0]
dy=[0,0,0,1,0,-1]
dh=[1,-1,0,0,0,0]
def bfs():
    while q:
        e,y,x=q.popleft()
        for i in range(6):
            ee,yy,xx=e+dh[i],y+dy[i],x+dx[i]
            if 0<=xx<m and 0<=yy<n and 0<=ee<h and tomato[ee][yy][xx]==0:
                tomato[ee][yy][xx]=tomato[e][y][x]+1
                q.append((ee,yy,xx))
                
#-----------------------  
#m=행,n=열,h=높이
m,n,h=map(int,input().split())
#1:익토, 0:안악토, -1:토마토x
tomato=[[list(map(int,input().split())) for _ in range(n)]for _ in range(h)]
q=deque()
num=0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j]==1:
                q.append((k,i,j))
                
bfs()                
res=-987654321000               
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j]==0:
                print(-1)
                sys.exit()
            res=max(res,tomato[k][i][j])
print(res-1)