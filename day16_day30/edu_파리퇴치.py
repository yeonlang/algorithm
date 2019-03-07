import sys
sys.stdin = open("파리퇴치.txt","r")

for tc in range(int(input())):
    n,m = map(int,input().split())
    data = [ list(map(int,input().split())) for _ in range(n) ]
    my_max = 0
    for start_x in range(0,n-m+1):
        for start_y in range(0,n-m+1):
            count = 0
            for y in range(start_y,start_y+m):
                for x in range(start_x,start_x+m):
                    count+=data[y][x]
            if count>my_max:
                my_max = count

    print("#{} {}".format(tc+1,my_max))

#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242
