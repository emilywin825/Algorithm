from collections import deque 

n=int(input())
arr=list(map(int,input().split()))

dir=[]

now=0
small=0

while arr:

    lt=arr[0]
    rt=arr[-1]

    small=lt if lt<rt else rt

    if(now>lt and now>rt):
        break
    else:
        if(now<lt and now<rt):


print(len(dir))
print(''.join(map(str,dir)))
