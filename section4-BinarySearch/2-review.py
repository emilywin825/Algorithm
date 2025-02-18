k, n = map(int, input().split())
arr=[int(input()) for _ in range(k)]

lt=1
rt=max(arr)
answer=0

while lt<=rt:
    sum=0
    mid=(lt+rt)//2
    for i in arr:
        sum+=i//mid

    if(sum>=n):
        answer=mid
        lt=mid+1
    else:
        rt=mid-1

print(answer)
