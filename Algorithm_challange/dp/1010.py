def pr(k,number) : 
    print('#' + str(k+1)+ ' ' + str(number))

total = int(input())

for k in range(total) : 
    N, D, X = map(int, (input().split()))
    array = list(map(int, (input().split())))
    number = 1
    i = D
    test = array[D-1]
    for j in range(500):
        number+=1
        i+=1
        
        if(i>N-1) : 
            i=0
        if i==D : 
            test = test-1
        if (test==0 and i==X-1) : 
            pr(k,number)
            break