# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.
#  ▣입력설명
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50) 
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다. 
# ▣출력설명
# 최대합을 출력합니다.
#  ▣입력예제 1                                   
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
#  ▣출력예제 1
#  155

# 행의 합 : array 인덱스 하나씩의 합
# 열의 합 : 
# 대각선의 합 : 

N = int(input())

array=[]

for _ in range(N):
    array.append(list(map(int,input().split())))

result = -1

# 행의 합
for i in array: 
    if result<sum(i):
        result = sum(i)

# 열의 합 [0][0] + [1][0] + [2][0]
for i in range(N):
    total = 0
    for j in range(N):
        total+=array[j][i]
    
    if result<total:
        result=total

# 왼쪽 시작 대각선
sum1=0
sum2=0
for i in range(N):
    sum1+=array[i][i]
    sum2+=array[i][N-1-i] 

if result<sum1:
    result=sum1
if result<sum2:
    result=sum2


print(result)