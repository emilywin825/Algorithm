def dfs(v): #v : 노드 번호
    global cnt
    if v==n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1,n+1): #i : 방문하려는 노드 번호
            if adj[v][i]==1 and ch[i]==0: #V노드에서 i번으로 갈 수 있는지  
                ch[i]=1
                path.append(i)
                dfs(i)
                path.pop()
                ch[i]=0

if __name__=="__main__":
    n,m=map(int,input().split())
    adj=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)
    for _ in range(m):
        a,b=map(int,input().split())
        adj[a][b]=1
    cnt=0
    ch[1]=1 #1번 노드 방문했다고 체크하고
    path=list()
    path.append(1)
    dfs(1) #1번 노드로 넘어간다.
    print(cnt)




# [0, 0, 0, 0, 0, 0] 
# [0, 0, 1, 1, 1, 0] 
# [0, 1, 0, 1, 0, 1] 
# [0, 0, 0, 0, 1, 0] 
# [0, 0, 1, 0, 0, 1]
# [0, 0, 0, 0, 0, 0]