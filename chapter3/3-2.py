
N, M, K = map(int, (input().split()))
data = list(map(int, (input().split())))

data.sort(reverse=True)  # 큰수부터 정렬
first = data[0]  # 첫번째 큰수
second = data[1]  # 두번째 큰수

#가장 큰수를 더해야 하는 횟수
count = int(M/(K+1))*K
count+= int(M%(K+1))

result = 0
result = (count * first) + (M-count)*second #두번째 큰수를 더해야 하는 횟수 : M-가장 큰 수를 더한 횟수

print(result)
