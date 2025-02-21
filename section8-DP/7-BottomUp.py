# N*N의 돌다리
# 이동 시 돌의 높이 만큼 에너지가 소비
# 오른쪽/아래로만 이동 가능
# (1,1) ->(N*N)까지 가는데 드는 에너지의 최소량
# 모든 경로를 탐색할 필요 없이 나의 오른쪽/아래쪽만 비교해서 가장 작은 값을 찾아가면 됨

n=int(input())
bridge=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
dp[0][0]=bridge[0][0]

for i in range(1,n):
    dp[i][0]=dp[i-1][0]+bridge[i][0]
    dp[0][i]=dp[0][i-1]+bridge[0][i]

for i in range(1,n): 
    for j in range(1,n):
        dp[i][j]=bridge[i][j]+min(dp[i-1][j],dp[i][j-1])
        
print(dp[n-1][n-1])    


# 5
# 3 7 2 1 9
# 5 8 3 9 2
# 5 3 1 2 3
# 5 4 3 2 1 
# 1 7 5 2 4
