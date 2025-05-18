import sys
input=sys.stdin.readline
from collections import deque

def bfs(node):
    global cnt
    q.append(node)
    visited[node]=cnt
    while q:
        now=q.popleft()
        for n in graph[now]:
            if visited[n]==0:
                cnt+=1
                visited[n]=cnt
                q.append(n)

n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for node in graph:
    node.sort()
visited=[0]*(n+1)
q=deque()
cnt=1

bfs(r)

for i in range(1,n+1):
    print(visited[i])