import sys
input=sys.stdin.readline
from collections import deque

def dfs(node):
        dfs_visited.append(node)
        for n in graph[node]:
            if n not in dfs_visited:
                dfs(n)
    
def bfs(node):
    bfs_visited.append(node)
    q.append(node)
    while q:
        now=q.popleft()
        for n in  graph[now]:
            if n not in bfs_visited:
                q.append(n)
                bfs_visited.append(n)

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
dfs_visited=[]
bfs_visited=[]
q=deque()

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for node in graph:
    node.sort()

dfs(v)
bfs(v)

print(*dfs_visited)
print(*bfs_visited)
