import sys
input=sys.stdin.readline

def dc(x,y,n):
    global res
    if n==0:
        return
    size=2**(n-1)
    if r<x+size and c<y+size:
        dc(x,y,n-1)
    elif r<x+size and c>=y+size:
        res+=size*size
        dc(x,y+size,n-1)
    elif r>=x+size and c<y+size:
        res+=2*size*size
        dc(x+size,y,n-1)
    else:
        res+=3*size*size
        dc(x+size,y+size,n-1)

n,r,c=map(int,input().split())
res=0
dc(0,0,n)
print(res)