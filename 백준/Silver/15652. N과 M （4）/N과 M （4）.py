def dfs(num,arr):
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(num,n+1):
        arr.append(i)
        dfs(i,arr)
        arr.pop()

n,m=map(int,input().split())
dfs(1,[])