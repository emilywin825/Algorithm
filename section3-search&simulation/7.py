# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 
# 있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사
# 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 
# 남겨놓는다.
# 현수과 수확하는 사과의 총 개수를 출력하세요.
#  ▣입력설명
# 첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20) 
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 
# 이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
# 각 격자안의 사과의 개수는 100을 넘지 않는다.
#  ▣출력설명
# 수확한 사과의 총 개수를 출력합니다.
#  ▣입력예제 1                                   
# 5
# [0][2]
# [1][1] [1][2] [1][3]
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
#  ▣출력예제 1
#  379

# 첫번째 열의 중간 값을 찾음
# 그걸 기준으로 양옆의 값 하나씩 찾아서 더함

array = []
N = int(input())
for _ in range(N):
    array.append(list(map(int,input().split())))

middle = N//2
result = 0

for i in range(middle+1):
    if(i==middle):
        first_new = array[i][middle-i:middle+i+1]
        result+=sum(first_new)
    else:
        first_new = array[i][middle-i:middle+i+1]
        second_new = array[N-i-1][middle-i:middle+i+1]
        result += sum(first_new) + sum(second_new)

print(result)