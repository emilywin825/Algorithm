n=int(input())
wine=[int(input()) for _ in range(n)]
dp=[0]*n
dp[0]=wine[0]

if n>1:
    dp[1]=wine[0]+wine[1]

    for i in range(2,n):
        #연속 2개 마시던가, 하나 건너뛰고 마시던가
        dp[i]=max(dp[i-3]+wine[i-1]+wine[i],dp[i-2]+wine[i],dp[i-1])
    
print(dp[-1])