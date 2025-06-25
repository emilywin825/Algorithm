from collections import deque
import sys
input=sys.stdin.readline

def bfs(start,num):
    q=deque()
    q.append((start,num))
    while q:
        x,num=q.popleft()
        if x==k:
            print(num)
            sys.exit()
        else:
            if visited[x]==0 and 0<=x<=100000:
                visited[x]=1
                q.append((x-1,num+1))
                q.append((x+1,num+1))
                q.append((x*2,num+1))
        
n,k=map(int,input().split())
visited=[0]*(200001)
bfs(n,0)
