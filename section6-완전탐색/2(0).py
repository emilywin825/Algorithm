# - 트리 구조 탐색 방법
# DFS, BFS가 있음

# 재귀를 이용한 DFS

# 전위 순회 : 루트>왼>오
def DFS(v):
    if v>5:
        return
    else:
        print(v,end=' ')
        DFS(v*2) #왼쪽 노드 호출
        DFS(v*2+1) #오른쪽 노드 호출
DFS(1)

# 중위 순회 : 왼>루트>오
def DFS(v):
    if v>5:
        return
    else:
        DFS(v*2) #왼쪽 노드 호출
        print(v,end=' ')
        DFS(v*2+1) #오른쪽 노드 호출
DFS(1)

# 후위 순회 : 왼>오>루트
def DFS(v):
    if v>5:
        return
    else:
        DFS(v*2) #왼쪽 노드 호출
        DFS(v*2+1) #오른쪽 노드 호출
        print(v,end=' ')
DFS(1)