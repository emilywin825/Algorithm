# 회의실 배정(그리디)
# 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하
# 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 단, 회의는 한번 시작하면 중간에 중
# 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
#  ▣입력설명
# 첫째 줄에 회의의 수 n(1<=n<=100,000)이 주어진다. 둘째 줄부터 n+1 줄까지 각 회의의 정
# 보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
#  ▣출력설명
# 첫째 줄에 최대 사용할 수 있는 회의 수를 출력하여라. 
# ▣입력예제 1                                   
# 5
# 4 6
# 1 4
# 2 3
# 5 7
# 3 5
#  ▣출력예제 1
#  3

n = int(input())

arr=[]
for i in range(n):
    start,finish=map(int,input().split())
    arr.append((start,finish))

arr.sort(key=lambda x : (x[1],x[0]))

result=0
finish_time=0

for s, f in arr:
    if finish_time<=s :
        result+=1
        finish_time=f

print(result)
