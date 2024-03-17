# 완전 탐색 : 모든 경우의 수를 주저 없이 다 계산하는 해결방법
# 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행
# 파이써에서의 실수형 변수는 유효숫자에 따라서 연산 결과가 원하는 값이 나오지 않을 수 있음

N = int(input())
data = list(map(str, input().split()))

X = Y = int(1)

for i in data:
    if (i == 'R' and Y <= N):
        Y += 1
    elif (i == 'L' and Y > 1):
        Y -= 1
    elif (i == 'U' and X > 1):
        X -= 1
    elif (i == 'D' and X <= 5):
        X += 1

print(X, Y)
