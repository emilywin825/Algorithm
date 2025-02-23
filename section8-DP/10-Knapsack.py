# 교환할 동전의 최소 개수

n=int(input())
coin=list(map(int,input().split()))
price=int(input())
dp=[501]*(price+1)
dp[0]=0
for i in range(n):
    # 2~15
    for j in range(coin[i],price+1):
        dp[j]=min(dp[j],dp[j-coin[i]]+1)
print(dp[price])

# 3
# 1 2 5
# 15