import sys
input=sys.stdin.readline

while True:
    n,m=input().split()
    n,m=int(n),int(round(float(m)*100))
    if n==0 and m==0:
        break

    dp=[0 for _ in range(m+1)]
    for _ in range(n):
        kcal,price=input().split()
        kcal,price=int(kcal),int(round(float(price)*100))
        for j in range(price,m+1):
            dp[j]=max(dp[j],dp[j - price] + kcal)

    print(dp[m])         