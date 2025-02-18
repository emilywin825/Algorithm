# 1 : 집, 0 : 집x
# dfs + dq

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global res
    res+=1
    apt[x][y]=0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<=n-1 and 0<=yy<=n-1 and apt[xx][yy]==1:
            dfs(xx,yy)

n=int(input())
apt=[list(map(int,input())) for _ in range(n)]
ch=list()
res=0
for i in range(n):
    for j in range(n):
        if apt[i][j]==1:
            res=0
            dfs(i,j)
            ch.append(res)
ch.sort()
print(len(ch))
for i in ch:
    print(i)

# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000