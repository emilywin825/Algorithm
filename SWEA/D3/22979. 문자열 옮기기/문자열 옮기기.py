T = int(input())
for test_case in range(1, T + 1):
    s=input()
    k=int(input())
    k_list=list(input().split())
    
    while k_list:
        now=int(k_list.pop(0))
        total=abs(now)%len(s)
        if now>0:
            s=s[total:]+s[0:total]
        elif now<0:
            s=s[len(s)-total:]+s[0:len(s)-total]
    print(s)