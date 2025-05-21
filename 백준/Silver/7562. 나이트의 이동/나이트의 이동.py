import sys
input=sys.stdin.readline
from collections import deque

T=int(input())
dx=[2,-1,1,-2,1,-2,2,-1]
dy=[1,2,-2,-1,2,1,-1,-2]

def bfs(x,y):
    q.append((x,y))
    while q:
        x,y=q.popleft()
        if x==des_x and y==des_y:
            print(visited[x][y])
            break
        for i in range(8):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<l and 0<=yy<l and visited[xx][yy]==0:
                visited[xx][yy]=visited[x][y]+1
                q.append((xx,yy))        

for _ in range(T):   
    l=int(input())
    start_x,start_y=map(int,input().split())
    des_x, des_y=map(int,input().split())
    visited=[[0]*l for _ in range(l)]
    q=deque()
    bfs(start_x,start_y)