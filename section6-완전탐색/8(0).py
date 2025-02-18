def dfs(L):
    global result
    if L==m:
        result+=1
        for i in ch:
            print(i,end=' ')
        print()
    else:
        for i in range(1,n+1):
            if arr[i]==0:
                arr[i]=1
                ch[L]=i
                dfs(L+1)
                arr[i]=0

n,m=map(int,input().split())
arr=[0]*(n+1)
ch=[0]*m
result=0
dfs(0)
print(result)