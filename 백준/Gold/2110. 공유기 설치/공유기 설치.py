n,c=map(int,input().split())
house=[int(input()) for _ in range(n)]
house.sort()
lt=1
rt=max(house)
max_dis=0
while lt<=rt:
    mid=(lt+rt)//2 #공유가 사이 거리
    cnt=1#공유기 개수
    current=house[0]
    for i in range(1,len(house)):
        if house[i]>=current+mid:
            cnt+=1
            current=house[i]
    if cnt>=c:
        lt=mid+1
        max_dis=mid
    else:
        rt=mid-1
        
print(max_dis)