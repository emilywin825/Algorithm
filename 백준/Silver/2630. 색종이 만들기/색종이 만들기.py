n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
white=0
blue=0
def splitt(x,y,n):
    global white, blue
    
    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                splitt(x,y,n//2)
                splitt(x,y+n//2,n//2)
                splitt(x+n//2,y,n//2)
                splitt(x+n//2,y+n//2,n//2)
                return
    if color==0:
        white+=1
    else:
        blue+=1
            
            
splitt(0,0,n)
print(white)
print(blue)