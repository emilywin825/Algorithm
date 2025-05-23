import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    while q:
        node=q.popleft()
        for i in tree[node]:
            if parent[i]==0:
                parent[i]=node
                q.append(i)

n=int(input())
parent=[0]*(n+1)
q=deque()
tree={}
for i in range(1,n+1):
    tree[i]=[]
    
for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

q.append(1)
parent[1]=1
bfs()
for i in range(2,n+1):
    print(parent[i])