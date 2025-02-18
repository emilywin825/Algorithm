# 계단을 올라갈 때 : +1, +2
# 1계단 : 1
# 2계단 : 2
# 3계단 : 1+1+1,1+2,2+1 : 3개
# 4계단 : 5개
# 5계단 : 1+1+1+1+1, 1+1+1+2, 1+2+1+1, 1+1+2+1, 2+1+1+1, 2+2+1, 2+1+2, 1+2+2 : 8개

#Top-Down 방식
def dfs(stairs):
    if dy[stairs]>0:
        return dy[stairs]
    if stairs==1 or stairs==2:
        return stairs
    else:
        dy[stairs]=dfs(stairs-1)+dfs(stairs-2)
        return dy[stairs]
n=int(input())
dy=[0]*(n+1)
print(dfs(n))

#Bottom-Up 방식
# n=int(input())
# dy=[0]*(n+1)
# dy[1]=1
# dy[2]=2
# for i in range(3,n+1):
#     dy[i]=dy[i-1]+dy[i-2]
# print(dy[n])