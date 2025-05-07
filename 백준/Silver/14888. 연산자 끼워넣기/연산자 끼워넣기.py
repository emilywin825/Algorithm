def cal(add,sub,mul,div,idx,sum):
    global maxx,minn
    if idx==n:
        maxx=max(sum,maxx)
        minn=min(sum,minn)
        return
    if add:
        cal(add-1,sub,mul,div,idx+1,sum+num[idx])
    if sub:
        cal(add,sub-1,mul,div,idx+1,sum-num[idx])
    if mul:
        cal(add,sub,mul-1,div,idx+1,sum*num[idx])
    if div:
        cal(add,sub,mul,div-1,idx+1,int(sum/num[idx]))

n=int(input())
num=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
maxx=-9876543000
minn=9876543000

cal(add,sub,mul,div,1,num[0])
print(maxx)
print(minn)