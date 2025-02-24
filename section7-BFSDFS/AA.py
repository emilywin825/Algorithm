# 0:빈칸, 1:집, 2:피자집
# 집의 피자배달 거리 : |x1-x2|+|y1-y2| 중 최소값
# 도시의 피자배달 거리 : 각 집의 피자배달 거리의 합
# 모든 거리를 다 비교해야 하므로 dfs

# 6개의 피자집 중 4개를 선택했을 때 도시의 피자배달 거리
# home=[(0, 1), (1, 0), (1, 3), (2, 2), (3, 2)]
# pizza=[(0, 2), (1, 2), (2, 1), (2, 3), (3, 0), (3, 3)]
def dfs(L,s):
    global res
    if L==m:
        sum=0 #도시의 피자배달 거리
        for h in home:
            dis=987600000 # 각 집의 피자 배달 거리
            for c in ch:
                dis=min(dis,abs(c[0]-h[0])+abs(c[1]-h[1])) # 각 집의 피자배달 거리를 구하고
            sum+=dis # 집의 피자배달 거리를 더해서 도시의 피자배달 거리를 구한다.
            if sum<res:
                res=sum
    else:
        for j in range(s,len(pizza)):
            ch[L]=pizza[j]
            dfs(L+1,j+1)

n,m=map(int,input().split())
map=[list(map(int,input().split())) for _ in range(n)]
res=98760000 #최종 결과값
now=0
home=list()
pizza=list()
ch=[0]*m

for i in range(n):
    for j in range(n):
        if map[i][j]==1:
            home.append((i,j))
        elif map[i][j]==2:
            pizza.append((i,j))

dfs(0,0)
print(res)

# 4 4
# 0 1 2 0
# 1 0 2 1
# 0 2 1 2
# 2 0 1 2