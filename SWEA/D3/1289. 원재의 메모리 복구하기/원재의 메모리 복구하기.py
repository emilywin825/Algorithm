T = int(input())
for test_case in range(1, T + 1):
    original=input()
    now='0'
    res=0
    
    for origin in original:
        if origin!=now:
            now=origin
            res+=1
    
    print(f"#{test_case} {res}")