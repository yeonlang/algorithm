import sys
sys.stdin = open('number_card.txt', 'r') #파일에서 읽을때 사용

for tc in range(int(input())):
    N=int(input())
    lst = list(map(int,input()))
    count=[0]*10
    my_max = 0

    for count_plus in lst:
        count[count_plus]+=1

    for check in range(9,-1,-1):
        if count[check] == max(count):
            print(f'#{tc + 1} {check} {count[check]}')
            break


