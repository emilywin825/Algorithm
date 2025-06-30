import sys
input=sys.stdin.readline
import heapq

n=int(input())
hw=[]
for _ in range(n):
    a,b=map(int,input().split())
    hw.append((a,b))
hw.sort()

q=[]
for deadline,ramen in hw:
    heapq.heappush(q,ramen)
    if len(q)>deadline:
        heapq.heappop(q)
        
print(sum(q))