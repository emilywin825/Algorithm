from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
farm=[list(map(int, input().split())) for _ in range(n)]
ch=set()
res=0
dQ=deque()
res+=farm[n//2][n//2]
dQ.append((n//2,n//2))
ch.add((n//2,n//2))
L=0
while True:
    if L==n//2:
        break
    for i in range(len(dQ)):
        node=dQ.popleft()
        for j in range(4):
            x=node[0]+dx[j]
            y=node[1]+dy[j]
            if (x,y) not in ch:
                res+=farm[x][y]
                ch.add((x,y))
                dQ.append((x,y))
    L+=1
print(res)
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19