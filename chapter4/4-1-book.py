n = int(input())

x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,-1,0,0]
move_type = ['L','R','U','D']

for plan in plans :
    for i in range(move_type) :
        if plan== move_type(i) :
           nx=x+dx(i)
           ny=y+dy(i)
    if(nx<1 or nx>n or ny<1 or ny>n) :
        continue

print(nx,ny)