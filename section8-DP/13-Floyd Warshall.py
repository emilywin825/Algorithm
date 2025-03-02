# 회원이 다른 모든 회원과 친구 : +1
# 회원이 다른 모든 회원의 친구 or 친구의 친구 : +2
# 회원이 다른 모든 회원의 친구 or 친구의 친구 or 친구의 친구의 친구: +3
# -> 노드에서 노드까지의 최단거리를 가깜움의 정도로 해라
# 회장 : 점수가 가장 작은 사람

n=int(input())
INF=789456000
dis=[[INF]*(n) for _ in range(n)] #회원끼리 가까움의 정도
maxx=9876540000
candidate=list()
for i in range(n):
    dis[i][i]=0

while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    else:
        dis[a-1][b-1]=1
        dis[b-1][a-1]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])

for i in range(n):
    if maxx>max(dis[i]):
        maxx=max(dis[i])
        candidate.clear()
        candidate.append(i+1)
    elif maxx==max(dis[i]):
        candidate.append(i+1)

print(maxx,len(candidate))
for i in candidate:
    print(i, end=' ')



# 5
# 1 2
# 2 3
# 3 4
# 4 5
# 2 4
# 5 3
# -1 -1