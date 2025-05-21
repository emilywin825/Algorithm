import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    while q:
        location,time=q.popleft()
        if location==k:
            print(time)
            return
        if location not in visited and 0<=location<=100000:
            visited[location]=True
            q.append((location-1,time+1))
            q.append((location+1,time+1))
            q.append((location*2,time+1))

n,k=map(int,input().split())
q=deque()
q.append((n,0))
visited={}
bfs()