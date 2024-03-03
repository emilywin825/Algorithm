import time

start_time = time.time()

N, M, K = map(int, (input().split()))
data = list(map(int, (input().split())))

data.sort(reverse=True)  # 큰수부터 정렬
first = data[0]  # 첫번째 큰수
second = data[1]  # 두번째 큰수

# 첫번째 큰수를 K번 더하고, 두번째 큰수를 1번 더하는 과정을 반복.
result = 0

while True:
    for i in range(K):  # 가장 큰 수를 K번 더함
        if M == 0: break
        M -= 1
        result += first
    if M == 0: break
    result += second
    M -= 1

print(result)

end_time = time.time()

print("time = ", end_time - start_time)
