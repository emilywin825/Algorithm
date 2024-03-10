N, K = map(int, input().split())
# N이 K의 배수이면 N/K를 실행
# 이외의 경우에는 N-1실행


result = 0
while True:
    if (N == 1): break
    # N이 K로 나누어 떨어진다면
    elif (N % K == 0):
        N = N / K
        result += 1
    else:
        N = N - 1
        result += 1

print(result)
