# 겹치지 않고 선을 연결하려면 연결하려는 선이 연결된 선보다 위에 있으면 안 됨 

n=int(input())
right=list(map(int,input().split()))
left=[i for i in range(1,n+1)]
dp=[0]*n
dp[1]=1

for i in range(1,n):
    maxx=0
    for j in range(i-1,-1,-1):
        if right[i]>right[j] and maxx<dp[j]:
            maxx=dp[j]
    dp[i]=maxx+1

print(max(dp))
# 10
# 4 1 2 3 9 7 5 6 10 8

# 10
# 3 2 5 4 1 6 10 9 7 8 