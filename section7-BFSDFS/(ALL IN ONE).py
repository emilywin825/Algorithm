
grid=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
visited=[
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]
cnt=0

def dfs(x,y):
    global visited
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    visited[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<len(grid) and 0<=yy<len(grid[0]) and grid[xx][yy]=="1" and visited[xx][yy]=="0":
            dfs(xx,yy)

if __name__=="__main__":
    for i in range(len(grid)): # 4
        for j in range(len(grid[0])): # 5
            if visited[i][j]=="0" and grid[i][j]=="1":
                dfs(i,j)
                cnt+=1

print(cnt)