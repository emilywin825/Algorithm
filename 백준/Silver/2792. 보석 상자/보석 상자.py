import sys
input=sys.stdin.readline

n,m=map(int,input().split())
color=[int(input()) for _ in range(m)]
lt=1
rt=max(color)
res=987654321000
while lt<=rt:
    jealousy=(lt+rt)//2
    num=0
    for c in color:
        num+=c//jealousy
        if c%jealousy>0:
            num+=1
    if num>n: #학생수보다 num이 크다
        lt=jealousy+1
    else:
        res=jealousy
        rt=jealousy-1
        
print(res)