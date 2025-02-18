# 섬 : 1 / 바다 : 0
# 상하좌우 대각선으로 연결 
# 총 몇개의 섬?
n=int(input())
island=[list(map(int,input().split())) for _ in range(n)]

def dfs(x,y):
    for i in range(len(dx)):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and island[xx][yy]==1:
            island[xx][yy]=0
            dfs(xx,yy)

dx=[-1,0,1,0,-1,1,-1,1]
dy=[0,1,0,-1,-1,-1,1,1]
 
res=0
for i in range(n):
    for j in range(n):
        if island[i][j]==1:
            island[i][j]=0
            dfs(i,j)
            res+=1
print(res)

# 7
# 1 1 0 0 0 1 0
# 0 1 1 0 1 1 0
# 0 1 0 0 0 0 0
# 0 0 0 1 0 1 1
# 1 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 0