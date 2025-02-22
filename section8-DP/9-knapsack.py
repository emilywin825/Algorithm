# 냅섹 알고리즘 -> 이거 매우 중요
n,max_p=map(int,input().split())
# dp[j] : 가방에 j무게 만큼 담을 때 보석의 최대가치
dp=[0]*(max_p+1)

for _ in range(n):
    w,p=map(int,input().split())
    for j in range(w,max_p+1):
        dp[j]=max(dp[j-w]+p, dp[j])

print(max(dp))

# 4 11
# 5 12
# 3 8
# 6 14
# 4 8

