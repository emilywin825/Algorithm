
N = int(input())

# 2xN
array = []


for i in range(N):
    age, name = input().split()
    array.append([int(age),name])

array.sort(key=lambda x :x[0])

for i in array:
    print(i[0],i[1])