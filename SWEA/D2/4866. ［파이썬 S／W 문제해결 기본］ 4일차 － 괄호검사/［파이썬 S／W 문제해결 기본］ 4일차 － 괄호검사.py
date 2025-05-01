T = int(input())
for test_case in range(1, T + 1):
    text=input()
    stack=[]
    res=1

    for target in text:
        if target in ['{', '(']:
            stack.append(target)
        elif target=='}':
              if not stack or stack[-1]!='{':
                   res=0
                   break
              stack.pop()
        elif target==')':
             if not stack or stack[-1]!='(':
                   res=0
                   break
             stack.pop()

    if stack:
        res=0
    print(f"#{test_case} {res}")