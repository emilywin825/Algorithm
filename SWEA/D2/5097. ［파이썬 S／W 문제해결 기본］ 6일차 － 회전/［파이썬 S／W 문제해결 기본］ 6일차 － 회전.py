T = int(input())
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    lis=list(map(int,input().split()))
    res=m%n
    print(f"#{test_case} {lis[res]}")
