# array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
array = list(range(1,21))

for _ in range(10):
    newarray = []
    reverse_array=[]

    a,b = map(int,input().split())

    newarray+=array[0:a-1]
    reverse_array = array[a-1:b]
    newarray+=reverse_array[::-1] 
    newarray+=array[b:]

    array = newarray

print(" ".join(map(str, array)))


