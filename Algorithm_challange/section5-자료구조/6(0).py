from collections import deque

n,m=map(int,input().split())
num=input().split()

arr = [[0 for j in range(2)] for i in range(n)]

for i in range(n):
    if i==m:
        arr[i][1]=1
    arr[i][0]=num[i]

arr=deque(arr)

cnt=1

while True:
    num=arr.popleft()
    maxx=max(arr)
    if num[0]>=maxx[0]:
        if num[1]==1:
            break  
        cnt+=1
    else:
        arr.append(num)

print(cnt)