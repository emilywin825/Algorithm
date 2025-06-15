import sys
input=sys.stdin.readline

T=int(input())
dp=[1]*10001
for i in range(2,4):
    for j in range(i,10001):
        dp[j]+=dp[j-i]
        
for _ in range(T):
    n=int(input())
    print(dp[n])