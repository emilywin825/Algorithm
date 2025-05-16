n=list(input())
arr=[]
sum_arr=[]
now=''
for i in range(len(n)):
    if n[i]=='+' or n[i]== '-':
        arr.append(int(now))
        arr.append(n[i])
        now=''
    else:
        now+=n[i]
arr.append(int(now))

for i in range(0,len(arr)):
    if arr[i]!='+':  
        sum_arr.append(arr[i])
    if arr[i-1]=='+':        
        res=sum_arr.pop()+sum_arr.pop()
        sum_arr.append(res)

answer=sum_arr[0]
for j in range(1,len(sum_arr)):
    if sum_arr[j]=='-':
        answer-=sum_arr[j+1]

print(answer)