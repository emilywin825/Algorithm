array = [list(map(int,input().split())) for _ in range(7)]

result =0

# 길이 5짜리 회문
for i in range(7):
    for j in range(3):
        colum = []
        row = []
        for k in range(5):
            colum.append(array[i][j+k])
            row.append(array[j+k][i])

        if(colum==colum[::-1]):
                result+=1        
        if(row==row[::-1]):
                result+=1

print(result)