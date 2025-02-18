key = input()
n=int(input())
key_arr=[x for x in key]

for i in range(1,n+1):
    subject=input()
    subject_arr=[]
    test_key=key_arr[:]
    for j in subject:
        if j in test_key:
            subject_arr.append(j)
            test_key.remove(j)
    if key_arr==subject_arr:
        print("#%d YES" %(i))
    else:
        print("#%d NO" %(i))
# # -----------------------------------