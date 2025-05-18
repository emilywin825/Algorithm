import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node):
    global cnt
    visited[node]=cnt
    for i in graph[node]:
        if visited[i]==0:
            cnt+=1
            dfs(i)

n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in graph:
    node.sort()

visited=[0]*(n+1)
cnt=1
dfs(r)

for i in range(1,n+1):
    print(visited[i])