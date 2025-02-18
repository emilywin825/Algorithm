n = int(input())
inverse_seq=list(map(int,input().split()))
# 5 3 4 0 2 1 1 0
seq=[0]*n

for i in range(n):
    cnt=0 # seq의 0의 개수 카운트
    index=0 # seq에 들어갈 인덱스 
    for j in range(n):
        if(seq[j]==0):
            cnt+=1

        if cnt==inverse_seq[i]+1 :
            seq[j]=i+1
            break

print(" ".join(map(str,seq)))