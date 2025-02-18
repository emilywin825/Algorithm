#top-down 방법
# 메모이제이션, 재귀 사용
def dfs(len):
    if dy[len] >0: # 가지치기
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[len]=dfs(len-1)+dfs(len-2) # 이렇게 메모이제이션하지 않으면 그냥 재귀함수 일 뿐
        return dy[len]

n=int(input())
dy=[0]*(n+1)
print(dfs(n))
print(dy)