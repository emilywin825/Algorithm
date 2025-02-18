n,m = map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()

lt=0
rt=n-1

while lt<=rt:
    mid= (lt+rt)//2
    if(m==arr[mid]):
        print(mid+1)
        break
    elif m<arr[mid] : #내가 찾으려는 값보다 중간값이 더 크다
        rt=mid-1

    else:
        lt=mid+1