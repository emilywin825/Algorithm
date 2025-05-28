k,n=map(int,input().split())
line=[int(input()) for _ in range(k)]
lt=1
rt=max(line)

answer=0
while lt<=rt:
    mid=(lt+rt)//2
    res=0
    for i in line:
        res+=i//mid
    if res>=n:
        answer=mid
        lt=mid+1
    else:
        rt=mid-1

print(answer)
