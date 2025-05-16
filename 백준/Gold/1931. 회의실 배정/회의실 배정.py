import sys
input=sys.stdin.readline

n = int(input())
coin=[]
for i in range(n):
    s,f=map(int,input().split())
    coin.append((s,f))
coin.sort(key=lambda x : (x[1],x[0]))

finish=-9876543210000
answer=0
for s,e in coin:
    if finish<=s:
        finish=e
        answer+=1

print(answer)
