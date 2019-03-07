import sys
sys.stdin = open("전개도.txt","r")

def Match(y1,x1,y2,x2):
    # x2와 y2를 큰 값으로 정렬
    if x1 > x2:
        x1,x2 = x2,x1
    if y1 > y2:
        y1,y2 = y2,y1

    # x 의 값이 2 차이가 난다면
    if x2 == (x1+2):
        # 사이에 건너갈 수 있는 숫자가 존재하는지 탐색
        # 만약 들어올때의 y2>y1 이었으면 위에서 아래로 한칸씩 내려가며 탐색
        # x2<x1 이면 아래에서 위로 한칸씩 올라가며 탐색(큰 값을 y2로 정렬하였기 때문에)
        for now in range(y1,y2+1):
            if a[now][x1+1] == 0:
                break
            if now >= y2:
                return 1

    # y 의 값이 2 차이가 난다면
    if y2 == (y1 + 2):
        # 사이에 건너갈 수 있는 숫자가 존재하는지 탐색
        # 만약 들어올때의 x2>x1 이었으면 위에서 아래로 한칸씩 내려가며 탐색
        # x2<x1 이면 아래에서 위로 한칸씩 올라가며 탐색(큰 값을 y2로 정렬하였기 때문에)
        for now in range(x1, x2 + 1):
            if a[y1+1][now] == 0:
                break
            if now >= x2:
                return 1
    return 0

a = [ list(map(int,input().split())) for _ in range(6) ]
result = [0] * 7
y_loca = [0] * 7
x_loca = [0] * 7

#1~6까지의 좌표를 x_loca , y_loca에 저장
for y in range(6):
    for x in range(6):
        y_loca[a[y][x]] = y
        x_loca[a[y][x]] = x

# 비교할 첫 번째 숫자를 고르고
for now_point in range(1,7):
    # 첫 번째 숫자의 페어 값이 아직 없다면
    if result[now_point] == 0:
        # 비교할 두 번째 숫자를 고른다.
        for nxt_point in range(now_point+1,7):
            # 두 번째 숫자의 페어 값도 없을 시
            if result[nxt_point] == 0:
                # 첫번째 포인트와 두번째 포인트의 좌표값으로 매치 되는 값인지 찾는다.
                if Match(y_loca[now_point], x_loca[now_point], y_loca[nxt_point], x_loca[nxt_point]):
                    # 매치가 된다면 결과 리스트에 페어 값을 넣어준다.
                    result[now_point] = nxt_point
                    result[nxt_point] = now_point
                    break

# 페어 값이 없는 숫자가 있다면 => 전개도가 아니다.
if 0 in result[1:]:
    print(0)
# 모든 페어가 맞는다면 1번과 짝이 되는 숫자를 print
else:
    print(result[1])
