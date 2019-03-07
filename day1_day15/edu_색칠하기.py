import sys
sys.stdin = open('sw4836.txt', 'r')

for tc in range(int(input())):
    check=[]
    arr=[ [0]*10 for _ in range(10)]
    for _ in range(int(input())):
        check.append(list(map(int, input().split())))

    for k in range(len(check)):
        for x in range(check[k][0],check[k][2]+1):
            for y in range(check[k][1],check[k][3]+1):
                arr[y][x]=arr[y][x] | check[k][4]

    my_sum=0
    for arr_y in arr:
        my_sum+=arr_y.count(3)

    print(f"#{tc+1} {my_sum}")





