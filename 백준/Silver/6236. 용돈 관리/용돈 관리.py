import sys
input=sys.stdin.readline

n,m=map(int,input().split())
money=[int(input()) for _ in range(n)]
lt=max(money)
rt=sum(money)
res=0

while lt<=rt:
    k=(lt+rt)//2
    hap=0
    num=1
    for i in money:
        if hap+i<=k:
            hap+=i
        else:
            num+=1
            hap=i
    if num>m:
        lt=k+1
    else:
        rt=k-1
        res=k
print(res)
        