N = int(input())

arr = []

for i in range(N):
    i,j = input().split()
    arr.append([int(i),int(j)])

arr.sort()

for i in arr:
    print(i[0],i[1])