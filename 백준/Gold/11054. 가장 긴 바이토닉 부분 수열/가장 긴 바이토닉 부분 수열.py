# 10
# 1 5 2 1 4 3 4 5 2 1

n=int(input())
arr=list(map(int,input().split()))
dp_left=[1]*(n) #i번째 인덱스가 마지막일 때 증가순열
dp_right=[1]*(n) #i번째 인덱스가 시작일 때 감소 순열
for i in range(n):
    for j in range(i-1,-1,-1):
        if arr[i]>arr[j]:
            dp_left[i]=max(dp_left[i],dp_left[j]+1)

for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        if arr[i]<arr[j]:
            dp_right[j]=max(dp_right[j],dp_right[i]+1)

new_dp=[0]*(n)
for i in range(n):
    new_dp[i]=dp_left[i]+dp_right[i]

print(max(new_dp)-1)