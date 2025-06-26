import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

#n:행,m:열,쓰레기개수:k
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(x,y):
    num=1
    for i in range(4):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<n and 0<=yy<m and visited[xx][yy]==0 and mapp[xx][yy]==1:
            visited[xx][yy]=1
            num+=dfs(xx,yy)
    return num
    
n,m,k=map(int,input().split())
mapp=[[0 for _ in range(m)] for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x,y=map(int,input().split())
    mapp[x-1][y-1]=1
res=0  
for i in range(n):
    for j in range(m):   
        if mapp[i][j]==1 and visited[i][j]==0:
            visited[i][j]=1
            res=max(res,dfs(i,j))

print(res)