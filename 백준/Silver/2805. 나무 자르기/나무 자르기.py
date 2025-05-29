import sys
input=sys.stdin.readline

n,m=map(int,input().split())
tree=sorted(list(map(int,input().split())))
lt=0
rt=max(tree)
max_height=0

while lt<=rt:
    mid=(lt+rt)//2
    height=0
    for t in tree:
        if t>mid:
            height+=t-mid
    if height>=m:
        lt=mid+1
        max_height=mid
    else:
        rt=mid-1
        
print(max_height)