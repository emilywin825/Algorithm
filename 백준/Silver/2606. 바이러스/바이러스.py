from collections import deque
import sys
input=sys.stdin.readline

def bfs(node):
    global cnt
    q.append(node)
    visited.append(node)
    while q:
        now=q.popleft()
        for n in graph[now]:
            if n not in visited:
                visited.append(n)
                q.append(n)

n=int(input())
pair=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(pair):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q=deque()  
visited=[]
bfs(1)
print(len(visited)-1)