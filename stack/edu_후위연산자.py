def push(x):
    global stack, top
    top+=1
    stack[top]=x

def pop():
    global stack, top
    top-=1
    print(stack[top+1], end="")
    stack[top+1] = 0

data = '(3-2*(6+5*(2-8)/2)+24)'
# data = input()
stack = [0]*10
top = -1
# ')':41, '*':42, '/':47, '+':43, '-':45 '(',40
icp={41:-1 ,42: 2 ,47: 2 ,43: 1 ,45: 1 ,40:3}
isp={41:-1 ,42: 2 ,47: 2 ,43: 1 ,45: 1 ,40:0}

for i in range(len(data)):
    if not ord(data[i]) in icp:
        print(data[i],end="")
        continue

    if icp[ord(data[i])] == -1:
        while stack[top] != '(':
            print(stack[top],end="")
            stack[top]=0
            top-=1
        stack[top]=0
        top-=1
        continue

    if top == -1:
        push(data[i])
    else:
        while True:
            if icp[ord(data[i])] <= isp[ord(stack[top])]:
                pop()
            else :
                push(data[i])
                break



