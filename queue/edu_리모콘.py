def func(n=10):
    global left,count
    count+=1
    print(count,f"현재 남은 값은 {left}입니다.")
    left -= n
    if left >= n :
        func(10)
    elif left >= 5:
        func(5)
    elif left >= 1:
        func(1)

count=0
start =7
end = 34
left = end-start

func()