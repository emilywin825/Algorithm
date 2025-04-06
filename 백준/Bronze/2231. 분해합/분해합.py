n=int(input())

for i in range(1,n):
    arr=list(map(int,str(i)))
    if i+sum(arr)==n:
        print(i)
        break

else:
    print(0)