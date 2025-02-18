# import sys
# input=sys.stdin.readline

# def dfs(L,s):
#     global total
#     if L==k :
#         if sum(res)%m==0:
#             total+=1
#     else:
#         for x in range(s,n):
#             res[L]=arr[x]
#             dfs(L+1,x+1)


# if __name__=="__main__":
#     n,k=map(int,input().split())
#     arr=list(map(int,input().split()))
#     m=int(input())
#     total=0
#     res=[0]*k
#     dfs(0,0)
#     print(total)

    
# # 5 3
# # 2 4 5 8 12
# # 6
import itertools as it

n,k=map(int,input().split())
arr=list(map(int,input().split()))
m=int(input())
total=0
for x in it.combinations(arr,k):
    if sum(x)%m==0:
        total+=1

print(total)