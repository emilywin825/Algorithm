# 9 3
# 1 2 3 4 5 6 7 8 9

# dvd가 몇 장 필요한지 return 해주는 함수
# capacity : dvd 용량
# cnt = 필요한 dbd 개수
def Count(capacity):
    cnt=1 
    sum=0
    for i in song:
        if sum+i>capacity:
            cnt+=1
            sum=i
        else:
            sum+=i
    return cnt

K,M = map(int,input().split())
song = list(map(int,input().split()))

lt= 1
rt=sum(song)
maxx=max(song)
result=0

while(lt<=rt):
    mid=(lt+rt)//2

    if Count(mid)<=M and mid>=maxx:
        result=mid
        rt = mid-1
    else: 
        lt=mid+1

print(result)