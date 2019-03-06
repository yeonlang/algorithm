import sys
sys.stdin = open("사칙연산.txt","r")

def cal(num1,num2,num3):
    if num2 == "+":
        return num1+num3
    elif num2 == "-":
        return num1-num3
    elif num2 == "*":
        return num1*num3
    elif num2 == "/":
        return num1/num3

for tc in range(10):
    n = int(input())
    tree = [0] * (n + 1)
    parents = [0] * (n + 1)
    l_child = [0] * (n + 1)
    r_child = [0] * (n + 1)
    brother = [0] * (n + 1)

    for _ in range(n):
        temp = list(input().split())
        if temp[1] not in ['+','-','*','/']:
            tree[int(temp[0])] = int(temp[1])
        else:
            tree[int(temp[0])] = temp[1]


        if len(temp)>2:
            parents[int(temp[2])] = int(temp[0])
            brother[int(temp[2])] = int(temp[3])
            parents[int(temp[3])] = int(temp[0])
            brother[int(temp[3])] = int(temp[2])
            l_child[int(temp[0])] = int(temp[2])
            r_child[int(temp[0])] = int(temp[3])

    for a in range(1,n+1):
        stack = []
        if l_child[a] == 0 and l_child[brother[a]]==0 and (a,brother[a]) not in stack and (brother[a],a) not in stack:
            stack.append((a,brother[a]))

    while stack:
        a,b = stack.pop()
        num2 = tree[parents[a]]
        num1 = tree[l_child[parents[a]]]
        num3 = tree[r_child[parents[a]]]
        tree[parents[a]] = cal(num1,num2,num3)
        tree[l_child[parents[a]]] = 0
        tree[r_child[parents[a]]] = 0
        l_child[parents[a]] = 0
        r_child[parents[a]] = 0
        if tree[1] not in ['+','-','*','/']:
            break
        for a in range(1,n+1):
            if tree[a] != 0 and l_child[a] == 0 and l_child[brother[a]]==0 and (a,brother[a]) not in stack and (brother[a],a) not in stack:
                stack.append((a,brother[a]))


    print("#{} {}".format(tc+1,int(tree[1])))

#1 13
#2 20
#3 35
#4 107
#5 369
#6 76
#7 123
#8 313
#9 238
#10 2



