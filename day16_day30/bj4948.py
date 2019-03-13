data = [i if i > 1 else 0 for i in range(246913)]

for i in range(2, 246913):
    if data[i] != 0:
        n = 2
        while i * n < len(data):
            data[i * n] = 0
            n += 1

while True:
    N =int(input())
    if N == 0 :
        break

    result = data[N+1:2*N+1]
    print(len(result)-result.count(0))



