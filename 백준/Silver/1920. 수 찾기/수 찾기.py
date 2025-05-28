n=int(input())
a=list(map(int,input().split()))
m=int(input())
data=list(map(int,input().split()))
dic={}
for i in a:
    dic[i]=True
    
for j in data:
    if j in dic:
        print(1)
    else:
        print(0)