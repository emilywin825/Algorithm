# 이분탐색 -> 결정알고리즘 사용할 때 쓸 수 있음

K, N = map(int,input().split())

array=[int(input()) for _ in range(K)]
lt = 1
rt = max(array)

answer = 0
while(lt<=rt):
    mid = (lt+rt)//2
    result = 0
    for ar in array:
        result+= ar//mid
    
    if(result>=N):
        answer = mid
        lt = mid+1
    else:
        rt = mid-1

print(answer)
