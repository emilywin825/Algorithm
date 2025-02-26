# 도시수 : n, 도로수 m
# 도로 정보 | 비용
# 자기자신으로 가는 비용 : 0, i번 정점에서 j번 정점으로 갈 수 없을 때 : m으로 출력
# 모든 도시에서 모든 도시로 이동하는 데 드는 최소 비용을 출력

# 플로이드-워셜 알고리즘 : 모든 정점에서 모든 정점까지의 최단 거리를 구하는 알고리즘
# 1. 처음에 인접행렬만 초기화하고, 인접하지 않은 곳은 9876000과 같이 큰 수로 초기화
# 2. i->j로 한번에 이동하는 거리와, K를 경유하면서 이동하는 거리 중 최소값으로 갱신한다.
# dis[i][j] : i노드에서 j노드로 이동할 때의 최소값 
# dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
n,m = map(int,input().split())
INF=98765000
dis=[[INF]*n for _ in range(n)] 

#자기자신으로 가는 비용
for k in range(n):
    dis[k][k]=0
#i->j로 바로 이동할 때 최소 비용
for k in range(m):    
    i,j,p=map(int,input().split())
    dis[i-1][j-1]=p
for i in range(n):
    for j in range(n):
        if dis[i][j]==INF:
            print("∞", end=' ')
        else:
            print(dis[i][j], end=' ')
# 플로이드-워셜 알고리즘
for k in range(n): #중간 지점 K
    for i in range(n):
        for j in range(n):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])

for i in range(n):
    for j in range(n):
        if dis[i][j]==INF:
            print("∞", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()


# 5 8
# 1 2 6
# 1 3 3
# 3 2 2
# 2 4 1
# 2 5 13
# 3 4 5
# 4 2 3
# 4 5 7