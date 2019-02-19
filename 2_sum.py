for tc in range(int(input())):
    lst=[]
    for _ in range(100):
        lst.append(list(map(int,input().split())))

    n=100
    result=[]
    cross1=0
    cross2=0

    for i in range(n):
        row_sum = 0
        column_sum = 0

        for j in range(n):
            row_sum +=lst[i][j]
            column_sum +=lst[j][i]

        result.append(row_sum)
        result.append(column_sum)

    for k in range(n):
        cross1 += lst[k][-(k+1)]
        cross2 += lst[k][k]

    result.append(cross1)
    result.append(cross2)

    print(f"#{tc+1} {max(result)}")