T = int(input())
k = int(input())
coins = [tuple(map(int, input().split())) for _ in range(k)]

dp = [0] * (T + 1)
dp[0] = 1

for coin, count in coins:
    # 기존 상태를 복사해서 새롭게 누적할 배열 사용
    new_dp = dp[:]
    for amount in range(coin, T + 1):
        for num in range(1, count + 1):
            if amount - coin * num < 0:
                break
            new_dp[amount] += dp[amount - coin * num]
    dp = new_dp  # 누적 결과 반영

print(dp[T])