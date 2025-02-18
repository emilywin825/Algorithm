paren=input()
paren=list(map(str,paren))


stack=[]
total=0
# ['(', ')', '(', '(', '(', '(', ')', '(', ')', ')', '(', '(', ')', ')', '(', ')', ')', ')', '(', '(', ')', ')']

for x in range(len(paren)):
    if paren[x]=='(':
        stack.append(x)
    else:
        stack.pop()
        if paren[x-1] =='(': #레이저
            total+=len(stack)
        else: #쇠막대기의 끝
            total+=1

print(total)