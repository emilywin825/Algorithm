import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    q=deque()
    q.append(0)
    visited[0]=True
    
    while q:
        now=q.popleft()
        x1,y1=mapp[now]
        
        for i in range(len(mapp)):
            if not visited[i]:
                x2,y2=mapp[i]
                if abs(x1-x2)+abs(y1-y2)<=1000:
                    visited[i]=True
                    q.append(i)
    

t=int(input())
for _ in range(t):
    n=int(input())#맥주를 파는 편의점의 개수
    #상근이 집, 편의점, 페스티벌
    mapp=[list(map(int,input().split())) for _ in range(n+2)]
    visited=[0]*(n+2)
    
    bfs()
    if visited[-1]==0:
        print("sad")
    else:
        print("happy")