for tc in range(int(input())):
    data = [ [0]*15 for _ in range(5)]
    for y in range(5):
        for x,value in enumerate(input()):
            data[y][x] = value

    print("#{}".format(tc+1),end=" ")
    for x in range(15):
        for y in range(5):
            if data[y][x] != 0:
                print(data[y][x],end ="")
    print()
