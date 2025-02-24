# 20시간 안에 풀 때 최대점수
# 점수 시간

n,m=map(int,input().split())
dp=[0]*(m+1)
for _ in range(n):
    sc,ti=map(int,input().split())
    for j in range(m,ti-1,-1):
        dp[j]=max(dp[j],dp[j-ti]+sc)
print(dp[m])

# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4