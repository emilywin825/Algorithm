N = int(input())

array = []

for i in range(N):
    weight, height = map(int, input().split())
    array.append((weight, height))

for i in array:
    number = 1
    for j in array:
        if i[0]<j[0] and i[1]<j[1]:
            number+=1
    print(number,end = " ")