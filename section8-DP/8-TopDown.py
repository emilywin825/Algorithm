def dfs(x,y):
    if dp[x][y]>0:
        return dp[x][y]
    if x==0 and y==0:
        return bridge[0][0]
    else:
        if x==0:
            dp[x][y]=dfs(x,y-1)+bridge[x][y]
        elif y==0:
            dp[x][y]=dfs(x-1,y)+bridge[x][y]
        else:
            dp[x][y]=min(dfs(x-1,y),dfs(x,y-1))+bridge[x][y]
        return dp[x][y]

n=int(input())
bridge=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
print(dfs(n-1,n-1))