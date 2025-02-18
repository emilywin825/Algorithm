def dfs(x,y):
    global result
    if x==6 and y==6:
        result+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and maze[xx][yy]==0 :
                maze[xx][yy]=1    
                dfs(xx,yy)
                maze[xx][yy]=0 # 왔던 길 다시 0으로 초기화화  


dx=[-1,0,1,0]
dy=[0,1,0,-1]
maze=[list(map(int,input().split())) for _ in range(7)]
result=0
maze[0][0]=1
dfs(0,0)
print(result)

# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 0 0 0 1
# 1 1 0 1 1 0 0
# 1 0 0 0 0 0 0