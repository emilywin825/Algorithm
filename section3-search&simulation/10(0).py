# 행에 중복이 없는지 -> eazy
# 열에 중복이 없는지 -> eazy
# 3x3에 중복이 없는지 -> not eazy

def check(array):
    for i in range(9):
        row_set = set()
        column_set = set()
        for j in range(9):
            row_set.add(array[i][j]) 
            column_set.add(array[j][i]) 
        if len(row_set)!=9 or len(column_set)!=9:
            return "NO"

    for i in range(3):
        for j in range(3):
            group=[0]*10
            for k in range(3):
                for s in range(3):
                    group[array[i*3+k][j*3+s]] = 1
        if(sum(group)!=9):
            return "NO"
                    
    return "YES"

array = [list(map(int,input().split())) for _ in range(9)]
print(check(array))