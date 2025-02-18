N = int(input())

# array = []
# for _ in range(N):
#     array.append(list(map(int,input().split())))

array = [list(map(int,input().split())) for _ in range(N)]

M = int(input())

for _ in range(M):
    row,direction,rotation = map(int,input().split())

    if(direction==0):
        for _ in range(rotation):
            array[row-1].append(array[row-1].pop(0))
    else:
        for _ in range(rotation):
            array[row-1].insert(0,array[row-1].pop())

result = 0
for i in range(N//2+1):
    if(i==N//2):
        result+=array[i][N//2]
    else:
        array_sum=sum(array[i][i:N-i])+sum(array[N-1-i][i:N-i])
        result += array_sum 

print(result)