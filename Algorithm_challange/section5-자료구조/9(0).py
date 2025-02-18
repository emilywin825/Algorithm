first=input()
second=input()
hash=dict()

for i in first:
    hash[i]=hash.get(i,0)+1

for j in second:
    hash[j]=hash.get(j,0)-1

for key,val in hash.items():
    if val>0:
        print("NO")
        break
else:
    print("YES")
