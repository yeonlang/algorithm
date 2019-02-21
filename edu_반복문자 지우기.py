for tc in range(int(input())):
    my_str=input()
    stack = [0]*1001
    top=-1

    for i in range(len(my_str)):
        if top>-1:
            if stack[top] == my_str[i]:
                stack[top] = 0
                top-=1
                continue
        top+=1
        stack[top]=my_str[i]

    print(f"#{tc+1} {len(stack)}")
