import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
m=int(input())

lt=1
rt=max(arr)
res=0
while lt<=rt:
    sum=0
    mid=(lt+rt)//2
    
    for target in arr:
        if target>mid:
            sum+=mid
        else:
            sum+=target
            
    if sum<=m:
        lt=mid+1
        res=mid
    else:
        rt=mid-1
        
print(res)
        
        
    
    