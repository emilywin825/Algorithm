# n=int(input()) #n은 홀수
# farm=[list(map(int,input().split())) for _ in range(n)]
# result=0
# start=n//2
# side=0
# for i in range(n//2+1): #i=0,1,2
#     for j in range(start-side,start+side+1):
#         if i==n//2:
#             result+=farm[i][j]
#         else:
#             result+=farm[i][j]
#             result+=farm[n-1-i][j]
#     side+=1

# print(result)

