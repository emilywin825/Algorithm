n=int(input())
atm=list(map(int,input().split()))
atm.sort()
answer=atm[0]
for i in range(1,n):
    atm[i]=answer+atm[i]
    answer=atm[i]
print(sum(atm))