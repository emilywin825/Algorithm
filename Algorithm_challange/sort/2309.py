import sys

def print_ans(list1,a,b):
    for i in range(9):
        if i==a or i==b:
            continue
        print(list1[i])

list1=[]
sum=0
for i in range(9):
    list1.append(int(input()))
    sum += list1[i]
        
list1.sort()


isTrue = False
for i in range(0,9):
    if isTrue : 
        break
    for j in range(i+1, 9):
        now = sum-list1[i]-list1[j]
        if  now == 100 :
            print_ans(list1,i,j)
            isTrue = True
            break