import sys
input=sys.stdin.readline
from collections import deque

def bfs(start,group):
    q=deque([start])
    visited[start]=group
    
    while q:
        node=q.popleft()
        for link_node in graph[node]:
            if not visited[link_node]:
                q.append(link_node)
                visited[link_node]=-visited[node]
            elif visited[link_node]==visited[node]:
                return True
    return False
    
#-----------------------------

k=int(input())
for _ in range(k):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited=[0 for _ in range(v+1)]
        
    for i in range(1,v+1):
        if visited[i]==0:
            res=bfs(i,1)
            if res:
                print("NO")
                break
    else:
        print("YES")
