# 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.
#  ▣입력설명
# 첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
# 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다. 
# 세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
# 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다. 
# 각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
#  ▣출력설명
# 오름차순으로 정렬된 리스트를 출력합니다.
#  ▣입력예제 1                                   
# 3
# 1 3 5
# 5
# 2 3 6 7 9
#  ▣출력예제 1
#  1 2 3 3 5 6 7 9

 
first_array=[]
second_array=[]

a = int(input())
first_array=list(map(int,input().split()))

b = int(input())
second_array=list(map(int,input().split()))

# 이렇게 sort로 정렬하면 nlogn의 시간복잡도

# new_array = first_array + second_array
# print(" ".join(map(str,sorted(new_array))))

# 근데 문제처럼 이미 정렬되어 있는 리스트를 합치는 경우 n번만에 합칠 수 있음
# [1,3,5]
# [2,3,6,7,9]

new_array=[]
if(len(first_array)>len(second_array)):
    num=len(first_array)
else:
    num=len(second_array)

for i in range(num):
    if(len(first_array)==0 or len(second_array)==0):
        break
    elif first_array[0]<=second_array[0]:
        data = first_array.pop(0)
        new_array.append(data)
    else:
        data = second_array.pop(0)
        new_array.append(data)

if(len(first_array)!=0):
    new_array+=first_array[0:]
else:
    new_array+=second_array[0:]

# print(" ".join(map(str,new_array)))
for x in new_array:
    print(x,end=' ')