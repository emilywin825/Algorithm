def solve(N):
    # 완전 이진 트리를 저장할 리스트 (1번부터 시작하니까 0번 인덱스는 버림)
    tree = [0] * (N + 1)
    numbers = list(range(1, N + 1))  # 1부터 N까지 숫자 준비
    idx = [1]  # 현재 tree에 넣을 인덱스를 저장하는 리스트 (리스트로 만든 이유: 재귀에서 값 공유하려고)

    # 중위 순회하면서 숫자 채워넣기
    def inorder(node):
        if node <= N:
            inorder(node * 2)  # 왼쪽 자식 방문
            tree[node] = numbers[idx[0] - 1]  # 현재 노드에 숫자 할당
            idx[0] += 1  # 다음 숫자를 준비
            inorder(node * 2 + 1)  # 오른쪽 자식 방문

    inorder(1)  # 루트 노드부터 중위 순회 시작

    # 문제에서 요구한 출력
    root_value = tree[1]       # 루트 노드(1번)의 값
    half_value = tree[N // 2]  # N//2 번 노드의 값

    print(root_value, half_value)

T = int(input())  # 테스트 케이스 개수
for test_case in range(1, T + 1):
    N = int(input())
    print(f"#{test_case} ", end="")
    solve(N)
