n = input()

stack=[]
for i in n:
    if n.isdecimal():
        stack.append(int(n))
    else:
        right=stack.pop()
        left=stack.pop()
        if n=='+':
            stack.append(left + right)
        elif n=='-':
            stack.append(left - right)
        elif n=='*':
            stack.append(left*right)
        elif n=='/':
            stack.append(left / right)

print(stack.pop())