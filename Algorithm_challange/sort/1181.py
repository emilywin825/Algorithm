def quick_sort(array):
    if len(array)<=1 : 
        return array
    pivot = array[len(array)//2]
    low, equal, high = [], [], []

    for num in array:
        if num<pivot:
            low.append(num)

        elif num==pivot:
            equal.append(num)

        elif num>pivot:
            high.append(num)
    return quick_sort(low)+equal+quick_sort(high)    

def quick_sort_len(array):
    if len(array)<=1 : 
        return array
    pivot = array[len(array)//2]
    low, equal, high = [], [], []

    for num in array:
        if len(num)<len(pivot):
            low.append(num)

        elif len(num)==len(pivot):
            equal.append(num)

        elif len(num)>len(pivot):
            high.append(num)
    return quick_sort(low)+equal+quick_sort(high)          


N = int(input())

array = []

for i in range(N) : 
    array.append(input())

array = list(set(array))
array = quick_sort_len(array)
print("------------------")
print(array)

# N = int(input())
# array = []

# for i in range(N):
#     array.append(input())
# array = list(set(array))
# array.sort()
# array.sort(key = len)

# for i in array:
#       print(i)