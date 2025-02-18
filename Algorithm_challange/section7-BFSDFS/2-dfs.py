def dfs(L,price):
    global res
    if L==n+1:
        if price>res:
            res=price
    else:
        if L+day_arr[L]<=n+1:
            dfs(L+day_arr[L],price+price_arr[L])
        dfs(L+1,price)

n=int(input())
day_arr=[0]
price_arr=[0]
for i in range(1,n+1):
    t,p=map(int,input().split())
    day_arr.insert(i,t)
    price_arr.insert(i,p)
res=-24700000
dfs(1,0)
print(res)

# 7
# 4 20 
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10