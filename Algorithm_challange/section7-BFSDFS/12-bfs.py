from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs():
    global res
    while Q:
        node=Q.popleft()
        for i in range(4):
            xx=node[0]+dx[i]
            yy=node[1]+dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and apt[xx][yy]==1:
                res+=1
                apt[xx][yy]=0
                Q.append((xx,yy))

n=int(input())
apt=[list(map(int,input())) for _ in range(n)]
Q=deque()
ch=list()
res=1

for i in range(n):
    for j in range(n):
        if apt[i][j]==1:
            apt[i][j]=0
            Q.append((i,j))
            bfs()
            ch.append(res)
            res=1

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