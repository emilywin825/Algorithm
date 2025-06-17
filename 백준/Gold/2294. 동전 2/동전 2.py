import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]
dp=[100001]*(k+1)
dp[0]=0

for c in coins:
    for money in range(c,k+1):
        dp[money]=min(dp[money],dp[money-c]+1)
        
if dp[k]==100001:
    print(-1)
else:
    print(dp[k])