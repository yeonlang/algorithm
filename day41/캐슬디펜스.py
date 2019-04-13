import sys
sys.stdin = open("캐슬디펜스.txt")

class Enemy:
    def __init__(self,y,x):
        self.y = y
        self.x = x
        self.dead = False

N,M,D = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(N)]

data = []
for y in range(N):
    for x in range(M):
        if Map[y][x]:
            data.append(Enemy(y,x))

myMax = 0
for n1 in range(M):
    for n2 in range(n1+1,M):
        for n3 in range(n2+1,M):
            cnt = 0
            for shooter_y in range(N,0,-1):
                result = set()
                for shooter_x in n1, n2, n3:
                    premax_val = 99
                    premin_x = 20
                    pre_y = 20
                    for i in range(len(data)):
                        enemy = data[i]
                        if not enemy.dead:
                            if enemy.y == shooter_y:
                                enemy.dead = True
                                continue
                            distance = abs(enemy.x - shooter_x) + abs(enemy.y-shooter_y)
                            if distance <= D and distance < premax_val:
                                premax_val = distance
                                premin_x = enemy.x
                                pre_y = enemy.y
                                idx = i
                            elif distance == premax_val and enemy.x < premin_x:
                                premin_x = enemy.x
                                pre_y = enemy.y
                                idx = i
                    if pre_y != 20:
                        result.add(idx)
                for j in result:
                    data[j].dead = True
                    cnt+=1
            for j in range(len(data)):
                data[j].dead = False
            if cnt>myMax:
                myMax = cnt
print(myMax)


