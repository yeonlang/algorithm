def jinsu(num,k):
    result = 0

    i = 1
    while num:
        result += i * (num % k)
        num = num//k
        i=i*10

    return result

print(jinsu(123,7))



