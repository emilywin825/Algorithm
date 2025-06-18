import sys
input=sys.stdin.readline
#n=행, m=열
n,m=map(int,input().split())
mapp=[list(map(int,input().split())) for _ in range(n)]
INF = int(1e9)
dp=[[[INF]*3 for _ in range(m)] for _ in range(n)]
for i in range(m):
    for j in range(3):
        dp[0][i][j]=mapp[0][i]


dy=[-1,0,1]
for i in range(1,n):
    for j in range(m):
        for cur_d in range(3):
            yy=j-dy[cur_d]
            if 0<=yy<m:
                for prev_d in range(3):
                    if cur_d!=prev_d:
                        dp[i][j][cur_d]=min(dp[i][j][cur_d],dp[i-1][yy][prev_d]+mapp[i][j])
res=INF                   
for l in range(m):
    res=min(res,min(dp[-1][l]))
print(res)