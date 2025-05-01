from collections import deque

dx=[0,1,0,-1]
dy=[-1,0,1,0]

def bfs(x,y):
    visited=[[0]*n for _ in range(n)]
    Q=deque()
    Q.append((x,y))

    while Q:
        x,y=Q.popleft()
        if (x,y)==end:
            return 1
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n:
                if visited[xx][yy]==0 and board[xx][yy]!=1:
                    visited[xx][yy]=1
                    Q.append((xx,yy))
    return 0

T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    board=[]
    start,end=0,0
    for i in range(n):
        lis=list(map(int,input()))
        if 2 in lis:
            start=(i,lis.index(2))
        if 3 in lis:
            end=(i,lis.index(3))
        board.append(lis)

    res=bfs(start[0],start[1])
    print(f"#{test_case} {res}")
