# 1. 문제의 Input을 받습니다.
# 2. 자신의 상,하,좌,우의 숫자와 비교한다.
# [0][0]이면 [0][1] / [1][0]이랑 비교 → 0이 하나라도 있으면 크기 비교 해줘야 함
# [1][1]이면 [0][1] / [2][1] / [1][0] / [1][2]
# 3. 자신의 상,하,좌,우보다 다 크다면 result +=1

N = int(input())

array = [[0] * (N+2)]
for i in range(N):
    input_array = list(map(int,input().split()))
    input_array.insert(0,0)
    input_array.append(0)
    array.append(input_array)
array.append([0]*(N+2))

result = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if(array[i][j]>array[i-1][j] and array[i][j]>array[i+1][j] and array[i][j]>array[i][j-1] and array[i][j]>array[i][j+1]):
            result+=1

print(result)

