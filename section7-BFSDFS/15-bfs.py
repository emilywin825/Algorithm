# 1: 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토 x
# m*n
# 토마토가 익을 때까지의 최소 날짜 / 저장될 때부터 모든 토마토 익어있으면 0 / 토마토가 모두 익지 못하는 상황 : -1
# 익은 토마토의 왼오앞뒤에 있는 토마토는 익은 토마토에 의해 익게 된다.
# 인접하다 : 왼오앞뒤에 있는 토마토

from collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs():
    global cnt
    while Q:
        node=Q.popleft()
        for i in range(4):
            x=node[0]+dx[i]
            y=node[1]+dy[i]
            if 0<=x<n and 0<=y<m and tomato[x][y]==0 and ch[x][y]==0:
                tomato[x][y]=1

m,n=map(int,input().split())
tomato=[list(map(int,input().split()))for _ in range(n)]
ch=[[0]*m for _ in range(n)]
res=-1 #토마토가 익는 날짜

Q=deque()
while True:
    for i in range(n):
        for j in range(m):
            if tomato[i][j]==1 and ch[i][j]==0:
                Q.append((i,j))
                ch[i][j]=1
    if len(Q)==m*n: #처음부터 다 익어있는 상태
        res=0
        break                
    elif len(Q)==0:
        break
    else:
        res+=1
        bfs()

if any(0 in row for row in tomato):
    res=-1

print(res)

# 6 4
# 0 0 -1 0 0 0
# 0 0 1 0 -1 0
# 0 0 -1 0 0 0
# 0 0 0 0 -1 1

# 3 3
# 1 1 1
# 1 1 1
# 1 1 1

# 3 3
# 1 -1 1
# -1 0 -1
# 1 -1 1