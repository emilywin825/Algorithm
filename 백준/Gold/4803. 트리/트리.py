import sys
input=sys.stdin.readline

def dfs(node,parent):
    global is_tree
    for i in tree[node]:
        if parent!=i and visited[i]==1:
            is_tree=False
        if visited[i]==0:
            visited[i]=1
            dfs(i,node)

test_case=0
while True:
    #n:정점, m:간선 
    test_case+=1
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    tree=[[] for _ in range(n+1)]
    visited=[0 for _ in range(n+1)]
    for _ in range(m):
        a,b=map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    res=0
    for i in range(1,n+1):
        if visited[i]==0:
            is_tree=True
            visited[i]=1
            dfs(i,i)
            if is_tree==True:
                res+=1
        
    if res==0:
        print("Case %d: No trees." %test_case)
    elif res==1:
        print("Case %d: There is one tree." %test_case)
    else:
        print("Case %d: A forest of %d trees." %(test_case, res))