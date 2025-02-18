# 앞1,뒤1,앞5
# 최소 몇번의 점프로 송아지 위치까지 갈 수 있는가?
# 현수위치S,송아지E
from collections import deque 

MAX=10000
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)
s,e=map(int, input().split())
ch[s]=1
dis[s]=0
dQ=deque()
dQ.append(s)

while dQ:
    now=dQ.popleft()
    if now==e:
        break
    for next in (now-1,now+1,now+5):
        if 1<=next<=MAX:
            if ch[next]==0:
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[e])