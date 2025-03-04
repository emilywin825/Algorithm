from collections import deque

n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)] # 각 노드의 진출 차수
indegree=[0]*(n+1) #각 노드의 진입 차수
res=[]
Q=deque()

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    indegree[b]+=1

# 1. 진입 차수가 0인 노드를 큐에 넣는다.
for i in range(1,n+1) :
    if indegree[i]==0:
        Q.append(i)

# 2.큐가 빌 때까지 다음의 과정을 반복한다.
while Q:
    # 2-1. 큐에서 원소를 꺼내서 출력
    now=Q.popleft()
    print(now, end=' ')
    for i in range(1, n+1):
        # 2-1. 해당 노드(now)의 진출차수를 제거한다.
        if graph[now][i]==1:
            indegree[i]-=1
        # 2-2. 새롭게 진입차수가 0이 된 노드를 큐에 삽입
            if indegree[i]==0:
                Q.append(i)

# 6 6
# 1 4 
# 5 4
# 4 3
# 2 5
# 2 3
# 6 2
