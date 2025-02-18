import sys
input=sys.stdin.readline

def dfs(L):
    global total
    if L==m:
        total+=1
        for i in ch:
            print(i,end=' ')
        print()

    else:
        for i in range(1,n+1):
            ch[L]=i
            dfs(L+1)

n,m=map(int,input().split())
total=0
ch=[0]*m
dfs(0)
print(total)