#0:빈칸,1:벽,2:바이러스
#바이러스 상하좌우로 이동
#벽은 꼭 3개 새워야 함
#n:행,m:열
#출력 : 0의 개수
from collections import deque
from itertools import combinations
import sys
input=sys.stdin.readline
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs():
    q=deque()
    for a,b in bacteria:
        q.append((a,b))
    while q:
        x,y=q.popleft()
        for i in range(4):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<n and 0<=yy<m and copy_mapp[xx][yy]==0:
                copy_mapp[xx][yy]=2
                q.append((xx,yy))
    cnt=0           
    for i in range(n):
        for j in range(m):
            if copy_mapp[i][j]==0:
                cnt+=1
    return cnt
                
    
n,m=map(int,input().split())
mapp=[list(map(int,input().split())) for _ in range(n)]
bacteria=[]
empty=[]
for i in range(n):
    for j in range(m):
        if mapp[i][j]==2:
            bacteria.append((i,j))
        if mapp[i][j]==0:
            empty.append((i,j))

res=-987654321000
for walls in combinations(empty,3):
    copy_mapp=[row[:] for row in mapp]
    for x,y in walls:
        copy_mapp[x][y]=1
    res=max(res,bfs())
print(res)