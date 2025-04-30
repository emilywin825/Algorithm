T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sum=0
    n=int(input())
    heap=list(map(int,input().split()))
    min_heap=[0]

    for i in heap:
        min_heap.append(i)
        num=len(min_heap)-1

        while num>1 and min_heap[num//2]>min_heap[num]:
            min_heap[num//2],min_heap[num]=min_heap[num], min_heap[num//2]
            num=num//2

    lenn=(len(min_heap)-1)//2
    while(lenn>0):
        sum+=min_heap[lenn]
        lenn//=2
    print(f"#{test_case} {sum}")
