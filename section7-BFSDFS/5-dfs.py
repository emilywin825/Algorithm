def dfs(L,a,b,c):
    global result

    if L==n:
        if a!=b and b!=c and c!=a:
            diff = max(a,b,c)-min(a,b,c)
            result=min(result,diff)
        return
    
    dfs(L+1,a+coin[L],b,c) #A에게 동전을 준다
    dfs(L+1,a,b+coin[L],c) #B에게 동전을 준다
    dfs(L+1,a,b,c+coin[L]) #C에게 동전을 준다

n=int(input())
coin=[int(input()) for _ in range(n)]
result=float('inf')
dfs(0,0,0,0)
print(result)

#백트래킹 조건
# 1. 동전의 합이 서로 같은 경우
# 2. 현재까지의 최소 차이보다 더 나쁜 경우를 만난 경우우