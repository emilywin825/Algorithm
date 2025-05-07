T = 10
for test_case in range(1, T + 1):
    seq=int(input())
    arr=list(map(int,input().split()))
    n=1
    while True:
        if n>5:
            n=1
        target=arr.pop(0)-n
        if target<=0:
            arr.append(0)
            break
        arr.append(target)
        n+=1
        
    print(f"#{seq}", *arr)