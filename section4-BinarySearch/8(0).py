from collections import deque

n,m = map(int, input().split())
wei = list(map(int, input().split()))

wei.sort()
# 50 60 70 90 100
wei=deque(wei)

result=0

while wei: #이렇게 while문을 설정하면 wei의 값이 없기 전까지 계속 반복한다.
    # num = len(wei)-1 -> 마지막 값 wei[num] == wei[-1] 
    if len(wei)==1:
        result+=1
        break
    if(wei[0]+wei[-1]>m):
        wei.pop()
    else:
        wei.popleft() #deque에서 가장 앞에 있는 변수를 pop하는 함수
        wei.pop()
    result+=1
        
print(result)

# deque : 앞뒤 양방향 모두에 데이터를 삽입/삭제 할 수 있는 자료구조
# list에서 pop(0)을 하면 뒤에 있는 값들이 모두 앞으로 이동하는 연산이 필요해서 비효율적이지만
# deque에서 pop(0)을 하면 포인터가 뒤로 이동하기 때문에 list의 pop연산보다 효율적