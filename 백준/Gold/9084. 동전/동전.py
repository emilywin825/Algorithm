T=int(input())
for _ in range(T):
    n=int(input())
    coin=list(map(int,input().split()))
    m=int(input())
    dp=[0]*(m+1)
    dp[0]=1
    for c in coin:
        for i in range(m+1):
            if c<=i:
                dp[i]+=dp[i-c]
    print(dp[m])