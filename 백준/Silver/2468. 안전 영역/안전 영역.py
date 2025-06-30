import sys
from collections import deque
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs(height,s_x,s_y):
    global visited
    q=deque()
    q.append((s_x,s_y))
    visited[s_x][s_y]=1    
    while q:
        x,y=q.popleft()
        for i in range(4):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<n and 0<=yy<n and mapp[xx][yy]>height and visited[xx][yy]==0:
                q.append((xx,yy))
                visited[xx][yy]=1

n=int(input())
mapp=[]
maxx=0
res=1
for i in range(n):
    arr=list(map(int,input().split()))
    maxx=max(maxx,max(arr))
    mapp.append(arr)
    
for rain in range(1,maxx+1):
    cnt=0
    visited=[[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mapp[i][j]>rain and visited[i][j]==0:
                cnt+=1
                bfs(rain,i,j)
    res=max(res,cnt)
    
print(res)