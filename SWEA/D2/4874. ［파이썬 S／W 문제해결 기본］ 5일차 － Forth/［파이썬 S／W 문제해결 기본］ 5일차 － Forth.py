T = int(input())
for test_case in range(1, T + 1):
    forth = input().split()
    stack = []
    answer = 'error'

    for i in forth:
        if i == '.':
            if len(stack) == 1:
                answer = stack[0]
            break
        elif i in ['+', '-', '*', '/']:
            if len(stack) < 2:
                break
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a // b)
        else:
            try:
                stack.append(int(i))
            except:
                break  # 숫자로 변환 안 되면 에러 처리

    print(f"#{test_case} {answer}")
