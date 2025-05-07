T = int(input())
for test_case in range(1, T + 1):
    arr=list(map(int,input().split()))
    arr.sort()
    arr.pop()
    arr.pop(0)
    res=round(sum(arr)/len(arr))
    print(f"#{test_case} {res}")