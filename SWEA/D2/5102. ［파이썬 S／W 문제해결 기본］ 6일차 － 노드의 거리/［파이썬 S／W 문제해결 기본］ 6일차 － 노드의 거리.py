from collections import deque

def bfs(s_node):
    Q=deque()
    Q.append(s_node)
    visited=[0]*(v+1)
    while Q:
        now=Q.popleft()
        if now==end:
            return visited[now]
        if now in tree:
            for nxt in tree.get(now):
                if visited[nxt]==0:
                    visited[nxt]=visited[now]+1
                    Q.append(nxt)
    return 0
            

T = int(input())
for test_case in range(1, T + 1):
    tree={}
    v,e=map(int,input().split())

    for _ in range(e):
        left,right=map(int,input().split())
        if left not in tree:
            tree[left]=[]
        tree[left].append(right)
        if right not in tree:
            tree[right]=[]
        tree[right].append(left)
    start,end=map(int,input().split())        

    res=bfs(start)
    print(f"#{test_case} {res}")