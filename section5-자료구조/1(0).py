n,m = map(int,input().split())
arr=list(map(int,str(n)))
# [5, 2, 7, 6, 8, 2, 3]
stack=[]

for x in arr:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

if m!=0:
    stack=stack[:-m]

print("".join(map(str,stack)))
# print(stack,end=' ')