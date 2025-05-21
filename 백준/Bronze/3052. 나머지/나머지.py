arr=[int(input()) for _ in range(10)]
remainder=set()
for a in arr:
    remainder.add(a%42)
    
print(len(remainder))