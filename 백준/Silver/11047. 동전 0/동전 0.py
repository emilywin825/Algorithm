n,k=map(int,input().split())
coin=[int(input()) for _ in range(n)]
coin.sort(reverse=True)
res=0

for i in range(n):
    if k//coin[i]>0:
        res+=k//coin[i]
        k%=coin[i]
        
print(res)