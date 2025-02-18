n=input()

stack=[]
res=''

for i in n:
    if i.isdecimal():
        res+=i
    else:
        if i=='(':
            stack.append(i)
        elif i==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
        elif i=='*' or i=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(i)
        elif i=='+' or i=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(i)


while stack:
    res+=stack.pop()

print(res)