def dfs(L,sum):
    global result
    if L>=result:
        return
    if sum>m:
        return
    if sum==m:
        if result>L:
            result=L
    else:
        for i in range(n):
            dfs(L+1,sum+coin[i])


n=int(input())
coin=list(map(int,input().split()))
m=int(input())
result=217000000
coin.sort(reverse=True)
dfs(0,0)
print(result)