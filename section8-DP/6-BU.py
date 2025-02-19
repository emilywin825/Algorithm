# 벽돌 회전x
# 밑면의 넓이,무게 다 다름 / 높이는 같을 수도 있음
# 밑면이 넓은 순으로 쌓아야 함
# 무게가 무거운 순으로 쌓아야 함
# 벽돌의 개수
# 벽돌 밑면의 넓이, 높이,무게
# bottom-up 방식 : 작은 인덱스에에 의해 내가 결정된다.

n=int(input())
brick=[list(map(int,input().split())) for _ in range(n)]
brick.sort()
dp=[0]*n
dp[0]=brick[0][1]
res=0

for i in range(1,n):
    maxx=0
    for j in range(i-1,-1,-1):
        if brick[j][2]<brick[i][2] and maxx<dp[j]:
            maxx=dp[j]
    dp[i]=maxx+brick[i][1]
    if res<dp[i]:
        res=dp[i]
print(res)

# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2
