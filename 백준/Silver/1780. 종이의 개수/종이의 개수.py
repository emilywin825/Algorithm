n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
minus,zero,one=0,0,0
def splitt(x,y,n):
    global minus,zero,one
    num=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num!=paper[i][j]:
                splitt(x,y,n//3)
                splitt(x,y+n//3,n//3)
                splitt(x,y+(n//3)*2,n//3)
                splitt(x+n//3,y,n//3)
                splitt(x+n//3,y+n//3,n//3)
                splitt(x+n//3,y+(n//3)*2,n//3)
                splitt(x+(n//3)*2,y,n//3)
                splitt(x+(n//3)*2,y+n//3,n//3)
                splitt(x+(n//3)*2,y+(n//3)*2,n//3)
                return
                
    if num==-1:
        minus+=1
    elif num==0:
        zero+=1
    else:
        one+=1
    
splitt(0,0,n)
print(minus)
print(zero)
print(one)