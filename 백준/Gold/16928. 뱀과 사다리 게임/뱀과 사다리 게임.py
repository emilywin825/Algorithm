import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    while q:
        now=q.popleft()
        if now==100:
            break
        for i in range(1,7):
            cur=now+i
            if cur in l_s:
                cur=l_s.get(cur)
            if 1<=cur<=100 and visited[cur]==0:
                visited[cur]=visited[now]+1
                q.append(cur)
                
                
n,m=map(int,input().split())
l_s={}

for _ in range(n+m):
    origin,move=map(int,input().split())
    l_s[origin]=move
q=deque()
visited=[0]*(101)

q.append(1)
bfs()
print(visited[100])