n=int(input())
lenn=list(map(int,input().split()))
price=list(map(int,input().split()))
total=price[0]*lenn[0]
cur_price=price[0]

for i in range(1,n-1):
    if cur_price > price[i]:
        cur_price=price[i]
    total+=lenn[i]*cur_price
print(total)