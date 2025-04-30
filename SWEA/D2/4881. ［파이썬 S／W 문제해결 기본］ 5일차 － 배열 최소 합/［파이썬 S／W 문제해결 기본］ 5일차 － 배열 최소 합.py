def backtrack(row, total):
    global minn
    if total >=minn:
        return
    if row==n:
        minn=min(total,minn)
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            backtrack(row+1,total+lis[row][i])
            visited[i]=False
    
T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    lis=[list(map(int,input().split())) for _ in range(n)]
    visited=[False]*n
    minn=float('inf')
    backtrack(0,0)
    print(f"#{test_case} {minn}")