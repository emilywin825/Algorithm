import sys
input=sys.stdin.readline

def calcul(arr):
    total=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            total=level[arr[i]-1][arr[j]-1]+level[arr[j]-1][arr[i]-1]+total
    return total

def make_link_arr(start_arr):
    link_arr=[]
    for i in range(1,n+1):
        if i not in start_arr:
            link_arr.append(i)
    return link_arr

def dfs(start):
    global minn
    for i in range(start,n+1):
        if len(start_arr)==n//2:
            link_arr=make_link_arr(start_arr)
            start=calcul(start_arr)
            link=calcul(link_arr)
            minn=min(minn,abs(start-link))
            return
        start_arr.append(i)
        dfs(i+1)
        start_arr.pop()

n=int(input())
level=[list(map(int,input().split())) for _ in range(n)]
start_arr=[]
minn=98765430000

dfs(1)
print(minn)