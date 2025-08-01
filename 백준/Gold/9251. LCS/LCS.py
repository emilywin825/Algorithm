import sys
input=sys.stdin.readline

a=list(input().strip())
b=list(input().strip())

LCS=[[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            LCS[i][j]=LCS[i-1][j-1]+1
        else:
            LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])

print(LCS[len(a)][len(b)])