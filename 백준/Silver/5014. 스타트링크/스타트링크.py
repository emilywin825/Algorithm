#f:최대층
#s층 -> g층으로 이동
#u:위, d:아래
import sys
input=sys.stdin.readline
from collections import deque

def bfs(start):
    q=deque()
    q.append((start,0))
    visited[start]=1
    while q:
        floor,num=q.popleft()
        if floor==g:
            return num
        if 1<=floor-d and visited[floor-d]==0:
            visited[floor-d]=1
            q.append((floor-d,num+1))
        if floor+u<=f and visited[floor+u]==0:
            visited[floor+u]=1
            q.append((floor+u,num+1))    
    return -1
    
f,s,g,u,d=map(int,input().split())
visited=[0]*(1000001)
res=bfs(s)
if res==-1:
    print("use the stairs")
else:
    print(res)