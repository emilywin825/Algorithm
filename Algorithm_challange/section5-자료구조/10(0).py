import heapq as hq

heap=[]

while True:
    n=int(input())

    if n==-1:
        break
    elif n==0:
        if len(heap)==0:
            print("-1")
        else:
            print(hq.heappop(heap))
    else:
        hq.heappush(heap,n)