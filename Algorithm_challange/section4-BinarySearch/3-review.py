n,m = map(int,input().split())
song=list(map(int,input().split()))

lt=1
rt=sum(song)
result=0
maxx=max(song)

while lt<=rt:
    cnt = 1 #디스크의 개수
    mid=(lt+rt)//2 #디스크 용량
    sum=0 #디스크에 저장된 용량

    for i in song:
        if(sum+i>mid):
            cnt+=1
            sum=0
        sum+=i

    if(cnt<=m and mid>maxx): # 디스크 개수가 제시된 것 보다 작으면 용량을 더 줄여야 한다는 것것
        result=mid
        rt=mid-1
    else:
        lt=mid+1

print(result)