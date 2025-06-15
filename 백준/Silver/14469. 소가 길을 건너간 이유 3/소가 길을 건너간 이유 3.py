n=int(input())
cow=[list(map(int,input().split())) for _ in range(n)]
cow.sort()
res=0
for arrive,check in cow:
    if res<arrive:
        res=arrive
    res+=check
    
print(res)