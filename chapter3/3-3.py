# min()함수 사용
N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_number = min(data)
    max(result, min_number)

print(result)
