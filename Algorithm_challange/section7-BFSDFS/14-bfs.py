# 안전 지역 : 물에 잠기기 않는 지점들이 위,아래,오른쪽,왼쪽으로 인접해 있으면서 그 크기가 최대인 영역
# 1<=높이<=100 
# 2~최대값까지 안전영역 개수 세는 거 다 해야함
# 격자판을 탐색하면서 특정 영역의 넓이 찾아내는 문제는 dfs,bfs 상관 없음

# from collections import deque
# dx=[1,0,-1,0]
# dy=[0,-1,0,1]

# def bfs():
#     while Q:
#         node=Q.popleft()
#         for i in range(4):
#             xx=node[0]+dx[i]
#             yy=node[1]+dy[i]
#             if 0<=xx<n and 0<=yy<n and area[xx][yy]>num and ch[xx][yy]==0:
#                 ch[xx][yy]=1
#                 Q.append((xx,yy))
                

# if __name__=="__main__":
#     n=int(input())
#     area=[list(map(int,input().split())) for _ in range(n)]
#     big=max(max(rows for rows in area))
#     num=0
#     maxx=-9876000
#     Q=deque()

#     while num<big:
#         res=0
#         ch=[[0]*n for _ in range(n)]
#         for i in range(n):    
#             for j in range(n):
#                 if area[i][j]>num and ch[i][j]==0:
#                     ch[i][j]=1
#                     Q.append((i,j))
#                     bfs()
#                     res+=1
#         if maxx<res:
#             maxx=res
#         num+=1
#     print(maxx)

from collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs():
    while Q:
        node=Q.popleft()
        for i in range(4):
            xx=node[0]+dx[i]
            yy=node[1]+dy[i]
            if 0<=xx<n and 0<=yy<n and area[xx][yy]>num and (xx,yy) not in ch:
                Q.append((xx,yy))
                ch.add((xx,yy))

if __name__=="__main__":
    n=int(input())
    area=[list(map(int,input().split())) for _ in range(n)]
    big=max(max(rows for rows in area))
    num=0
    maxx=-9876000
    Q=deque()

    while num<big:
        res=0
        ch=set()
        for i in range(n):    
            for j in range(n):
                if area[i][j]>num and (i ,j) not in ch:
                    ch.add((i,j))
                    Q.append((i,j))
                    bfs()
                    res+=1
        if maxx<res:
            maxx=res
        num+=1
    print(maxx) 

# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7