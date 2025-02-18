node,edge=map(int,input().split())
adj=[[0]*node for _ in range(node)]

for _ in range(edge):
    a,b,vertex=map(int,input().split())
    adj[a-1][b-1]=vertex

for x in range(node):
    for y in range(node):
        print(adj[x][y], end=' ')
    print()