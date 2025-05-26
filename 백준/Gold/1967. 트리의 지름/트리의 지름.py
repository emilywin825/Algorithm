import sys
input=sys.stdin.readline
from collections import deque

def bfs(start_node):
    visited=[-1 for _ in range(n+1)]
    q.append(start_node)
    visited[start_node]=0
    max_node=start_node
    while q:
        node=q.popleft()
        for child,dist in tree[node]:
            if visited[child]==-1:
                visited[child]=visited[node]+dist
                q.append(child)
                if visited[max_node]<visited[child]:
                    max_node=child
    return max_node, visited[max_node]
    
n=int(input())
tree={}
q=deque()
for i in range(n+1):
    tree[i]=[]
for _ in range(n-1):
    p,c,d = map(int,input().split())
    tree[p].append((c,d))
    tree[c].append((p,d))
    
first,_ = bfs(1)
_,diameter = bfs(first)
print(diameter)