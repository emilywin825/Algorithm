N, k = map(int,input().split())

# array = []

array = list(map(int,input().split()))    
array.sort(reverse = True)

print(array[k-1])