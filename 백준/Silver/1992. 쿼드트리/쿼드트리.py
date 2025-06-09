import sys
input=sys.stdin.readline

n=int(input())
quad=[list(map(int,input().strip())) for _ in range(n)]
res=''
def splitt(x,y,n):
    global res
    color=quad[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=quad[i][j]:
                res+='('
                splitt(x,y,n//2)
                splitt(x,y+n//2,n//2)
                splitt(x+n//2,y,n//2)
                splitt(x+n//2,y+n//2,n//2)
                res+=')'
                return
    res+=str(color)

splitt(0,0,n)   
print(res)