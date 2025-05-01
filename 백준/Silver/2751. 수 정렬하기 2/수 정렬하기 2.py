import sys
input = sys.stdin.readline  # 빠른 입력

n=int(input())
lis=[int(input()) for _ in range(n)]
lis.sort()
for i in lis:
    print(i)