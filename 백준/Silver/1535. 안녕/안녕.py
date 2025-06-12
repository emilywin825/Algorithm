n=int(input())
#체력,기쁨
#세준이 체력은 100
stamina=list(map(int,input().split()))
joy=list(map(int,input().split()))
dp=[0 for _ in range(100)]
for i in range(n):
    s=stamina[i]
    j=joy[i]
    for k in range(99,s-1,-1):
        dp[k]=max(dp[k],dp[k-s]+j)
        
print(max(dp))