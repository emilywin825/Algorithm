N = int(input())

array = []

for i in range(N) : 
    name,date,month,year = input().split()
    array.append([name,int(date),int(month),int(year)])

array.sort(key=lambda x : (x[3],x[2],x[1]))

youngest = array[N-1]
oldest = array[0]

# print(youngest[0])
# print(oldest[0])
print(array[N-1][0])
print(array[0][0])