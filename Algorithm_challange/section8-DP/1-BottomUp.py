# bottom-up 방법
# 반복문 사용
n=int(input())
dy=[0]*(n+1)
# 직관적으로 알 수 있는 것은 직접 초기화
dy[1]=1
dy[2]=2

for i in range(3,n+1):
    dy[i]=dy[i-2]+dy[i-1]

print(dy[n])