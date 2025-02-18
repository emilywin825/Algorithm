# def dfs(L):
#     global result
#     if L==m:
#         result+=1
#         for i in arr:
#             print(i,end=' ')
#         print()
#     else:
#         for i in range(1, n+1):
#                 if L==0 or arr[L-1]<i:
#                     arr[L]=i
#                     dfs(L+1)

def dfs(L,s):
    global result
    if L==m:
        result+=1
        for i in arr:
            print(i,end=' ')
        print()
    else:
        for i in range(s, n+1):
            arr[L]=i
            dfs(L+1,i+1)
    
if __name__=="__main__":
    n,m = map(int,input().split())
    arr=[0]*m #2개 뽑아서 넣을 리스트
    result=0
    dfs(0,1)
    print(result)