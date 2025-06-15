n,k=map(int,input().split())
coin=[int(input()) for _ in range(n)]
dp=[0 for _ in range(k+1)]
dp[0]=1
for c in coin:
    for amount in range(k+1):
        if c<=amount:
            dp[amount]+=dp[amount-c]
print(dp[k])