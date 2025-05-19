import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<m and visited[xx][yy]==0 and mapp[xx][yy]==1:
            visited[xx][yy]=1
            dfs(xx,yy)

T=int(input())
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for _ in range(T):
    m,n,k=map(int,input().split())
    mapp=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    answer=0

    for _ in range(k):
        y,x=map(int,input().split())
        mapp[x][y]=1

    for i in range(n):
        for j in range(m):
            if mapp[i][j]==1 and visited[i][j]==0:
                visited[i][j]=1
                answer+=1
                dfs(i,j)
    print(answer)
    