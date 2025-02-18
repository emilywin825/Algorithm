L = int(input())
hei = list(map(int,input().split()))
M=int(input())

hei.sort()

for i in range(M):
    hei[len(hei)-1]-=1
    hei[0]+=1
    hei.sort()

print(hei[len(hei)-1]-hei[0])