from collections import deque
import sys
input=sys.stdin.readline

def bfs(node):
    q=deque()
    visited=[-1]*(n+1)
    visited[node]=0
    q.append(node)
    while q:
        p=q.popleft()
        for i in family[p]:
            if visited[i]==-1:
                visited[i]=visited[p]+1
                if i==a:
                    return visited[i]
                q.append(i)
    return -1

n=int(input())
a,b=map(int,input().split())
m=int(input())
family=[[] for _ in range(n+1)]
for _ in range(m):
    #x는 y의 부모
    x,y=map(int,input().split())
    family[x].append(y)
    family[y].append(x)
print(bfs(b))
