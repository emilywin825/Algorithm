def dfs(n,count):
    global minn
    if n==1:
        minn=min(minn,count)
        return
    elif n<0:
        return
    if minn<=count:
        return
    if dp[n]:
        return dp[n]
    else:
        if n%3==0:
            dp[n]=dfs(n//3,count+1)
        if n%2==0:
            dp[n]=dfs(n//2,count+1)
        if n-1>1:
            dp[n]=dfs(n-1,count+1)
    
n=int(input())
dp=[0]*(n+1)
minn=9876543210000
dfs(n,0)
print(minn)