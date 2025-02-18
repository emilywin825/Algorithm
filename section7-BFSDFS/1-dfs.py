def dfs(L,sum,time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        dfs(L+1,sum+arr[L][0],time+arr[L][1]) #해당 문제를 푼다
        dfs(L+1,sum,time) #해당 문제를 풀지 않는다.

n,m=map(int,input().split())
arr=[[0]*2 for _ in range(n)]
for i in range(n):
    score, time=map(int,input().split())
    arr[i][0]=score
    arr[i][1]=time
res=-247000000
dfs(0,0,0)
print(res)

# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4