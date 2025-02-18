from collections import deque

n,m = map(int,input().split())
arr= list(range(1,n+1))
arr = deque(arr)

while arr:
    for _ in range(m-1):
        arr.append(arr.popleft())
    arr.popleft()

    if len(arr)==1:
        print(arr.popleft())