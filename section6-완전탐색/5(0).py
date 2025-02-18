def dfs(L,result,t_sum):
    global maxx
    if result+(total-t_sum)<maxx:
        return
    if result>c:
        return
    if L==n:
        if result>maxx:
            maxx=result
    else:
        dfs(L+1,result,t_sum+a[L])
        dfs(L+1,result+a[L],t_sum+a[L])

c, n = map(int,input().split())
a=[int(input()) for _ in range(n)]
result=0
maxx=0
total=sum(a)
dfs(0,0,0)
print(maxx)