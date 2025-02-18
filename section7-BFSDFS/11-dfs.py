# N*N / 각 구역에는 높이가 표시
# 다른구역으로 등산할 때는 위,아래,왼,오 중 더 높은 구역으로만 이동 가능
# 출발지 : 가장 낮은 곳 / 목적지 : 가장 높은 곳
# 등산 경로 개수를 구하시오 ->DFS
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global result
    if x==max_idx[0] and y==max_idx[1]:
        result+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and ch[xx][yy]==0 and maze[x][y]<maze[xx][yy]:
                ch[xx][yy]=1
                dfs(xx,yy)
                ch[xx][yy]=0 # dfs호출 전 했던 행동을 취소하려면 dfs 호출 후 다시 해주면 됨

n=int(input())
maze=[list(map(int,input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
minn=min(min(row) for row in maze) # 각 행마다 최솟값 찾고, 그 값들 중 최솟값을 찾음
maxx=max(max(row) for row in maze)
for i,row in enumerate(maze):
        if minn in row : 
            j=row.index(minn)
            min_idx=(i,j)
        if maxx in row : 
            j=row.index(maxx)
            max_idx=(i,j)
ch[min_idx[0]][min_idx[1]]=1
result=0
dfs(min_idx[0],min_idx[1])
print(result)


# 10
# 2 23 92 78 93 100 34 1 3 5
# 59 50 48 90 80 101 45 5 3 8
# 30 53 70 75 96 102 56 23 45 12
# 94 91 82 89 93 103 76 76 54 32
# 97 98 95 96 100 104 123 76 54 32
# 102 103 104 105 106 107 23 87 98 87
# 23 45 76 34 87 125 34 88 99 77
# 56 88 99 105 106 107 23 87 98 87
# 102 103 104 105 106 107 23 87 98 99
# 33 103 104 105 106 107 23 87 98 11