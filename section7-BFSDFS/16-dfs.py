#  2 : 도착지점, 1: 사다리 , 0 : x
#  도착지점에 도착하기 위해서는 몇 번째 열에서 출발해야 하는지
#  모든 경로 탐색 : dfs
# 사다리타기 : 아래,왼,오밖에 안됨
# dfs??

def dfs(x,y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        #왼
        if y-1>=0 and map[x][y-1]==1 and ch[x][y-1]==0:
            dfs(x,y-1)
        #오
        elif y+1<10 and map[x][y+1]==1 and ch[x][y+1]==0:
            dfs(x,y+1)
        #위
        elif x-1>=0 and map[x-1][y]==1 and ch[x-1][y]==0:
            dfs(x-1,y)


map=[list(map(int,input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
y=map[9].index(2)
map[9][y]=0
dfs(9,y)