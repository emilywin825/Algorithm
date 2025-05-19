import sys
input=sys.stdin.readline
from collections import deque

def bfs(x,y):
    cnt=1
    q.append((x,y))
    visited[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and visited[xx][yy]==0 and mapp[xx][yy]==1:
                visited[xx][yy]=1
                cnt+=1
                q.append((xx,yy))
    answer.append(cnt)
    
n=int(input())
mapp=[list(map(int,input().rstrip())) for _ in range(n)]

visited=[[0]*n for _ in range(n)]
answer=[]
q=deque()
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    for j in range(n):
        if mapp[i][j]==1 and visited[i][j]==0:
            bfs(i,j)

answer.sort()
print(len(answer))
for num in answer:
    print(num)

