import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
lt=max(arr)
rt=sum(arr)
res=1
while lt<=rt:
    blueray=(lt+rt)//2
    summ=0
    num=1
    for i in arr:
        if summ+i<=blueray:
            summ+=i
        else:
            summ=i
            num+=1
            
    if num>m:
        lt=blueray+1
    else:
        res=blueray
        rt=blueray-1
        
print(res)