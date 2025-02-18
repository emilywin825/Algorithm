N,M = map(int,input().split())

array = list(map(int,input().split()))
array.sort()
# cmt=0
# for i in range(0,N-1):   
#     idx=i
#     for j in range(i+1,N):
#         if(array[idx]>array[j]):
#             idx = j
#             cmt+=1
#     if(cmt==0):
#         break 
#     array[i], array[idx] = array[idx],array[i]
# print(array.index(M)+1)

lt=0
rt=N-1
while lt<=rt:
    mid = (lt+rt)//2
    if(array[mid]==M):
        print(mid+1)
        break
    elif(array[mid]<M):
        lt=mid+1
    else:
        rt=mid-1