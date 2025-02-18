import sys
input=sys.stdin.readline

import time
start_time = time.time() 

def dfs(L,sum):
    global result
    if sum>t:
        return
    if L==k:
        if sum==t:
            result+=1
    else:
        for i in range(n[L]+1):
            dfs(L+1,sum+(p[L]*i))
    

t=int(input())
k=int(input())
p=list()
n=list()
for _ in range(k):
   a,b=map(int,input().split())
   p.append(a)
   n.append(b)
result=0
dfs(0,0)
print(result)
end_time = time.time()  # 종료 시간 기록
print(f"실행 시간: {end_time - start_time:.5f}초")

# 20
# 3
# 5 3
# 10 2
# 1 5