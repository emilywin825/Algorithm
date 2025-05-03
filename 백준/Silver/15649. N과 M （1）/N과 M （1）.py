def dfs(arr):
    if len(arr)==m:
        for i in arr:
            print(i,end=' ')
        print()
        return
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            dfs(arr)
            arr.pop()
    

n,m=map(int,input().split())
dfs([])
