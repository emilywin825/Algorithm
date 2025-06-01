n=int(input())
line=sorted([list(map(int,input().split())) for _ in range(n)])
dp=[1]*n

for i in range(n):
    for j in range(i):
        if line[i][1]>line[j][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))