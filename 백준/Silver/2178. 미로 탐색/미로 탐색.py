import sys
input=sys.stdin.readline
from collections import deque

def bfs(x,y,num):
    q.append((x,y,num))
    visited[x][y]=num
    while q:
        x,y,num=q.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<m and visited[xx][yy]==0 and maze[xx][yy]==1:
                visited[xx][yy]=num+1
                if xx==n-1 and y==m-1:    
                    return
                visited[xx][yy]=num+1
                q.append((xx,yy,num+1))
    

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
maze=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
q=deque()
bfs(0,0,1)
# print(visited)
print(visited[n-1][m-1])