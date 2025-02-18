# bottom-up 방식으로????????

n=int(input())
arr=list(map(int,input().split()))
dp=[0]*n
dp[0]=1

for i in range(1,n): #비교대상
    maxx=0
    for j in range(i-1,-1,-1): #나보다 앞에 있는 인덱스의 값
        if arr[i]>arr[j] and maxx<dp[j]:
            maxx=dp[j]
    dp[i]=maxx+1
    
print(max(dp))

# 8
# 5 3 7 8 6 2 9 4
