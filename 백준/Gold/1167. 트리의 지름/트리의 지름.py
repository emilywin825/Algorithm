import sys
input=sys.stdin.readline
from collections import deque

def bfs(start):
    visited=[-1]*(n+1)
    q=deque()
    q.append(start)
    visited[start]=0
    maxx=start

    while q:
        now=q.popleft()
        for node,lenn in tree[now]:
            if visited[node]==-1:
                q.append(node)                
                visited[node]=visited[now]+lenn
                if visited[node]>visited[maxx]:
                    maxx=node
    return maxx, visited[maxx]

n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n):
    arr=list(map(int,input().split()))
    idx=arr[0]
    for j in range(1,len(arr)-1,+2):
        tree[idx].append((arr[j],arr[j+1]))


first_node,_=bfs(1)
_, diameter=bfs(first_node)
print(diameter)