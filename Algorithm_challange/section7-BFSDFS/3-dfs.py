def dfs(L,sum):
    global res
    if L==k:
        if 0<sum<=s:
            res[sum]=1
        return
    else:
        dfs(L+1,sum+arr[L])
        dfs(L+1,sum)
        dfs(L+1,sum-arr[L])

k=int(input())
arr=[int(i) for i in input().split()]
s=sum(arr)
res=[0]*(sum(arr)+1)
dfs(0,0)
print(res)
print(res.count(0)-1)