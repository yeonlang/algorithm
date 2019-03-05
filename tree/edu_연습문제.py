import sys
sys.stdin = open("연습문제.txt","r")

def dis(num1,num2):
    if level[num1]>level[num2]:
        num1,num2 = num2,num1
    # num1,num3 가 위쪽 num2,num4 가 아래쪽
    num3 = num1
    num4 = num2

    while num3 and num4:
        if level[num4] == level[num3]:
            break
        else:
            num4=parents[num4]

    while num3 and num4:
        if num3 == num4:
            root = num3
            break
        else:
            num3 = parents[num3]
            num4 = parents[num4]

    return abs(level[root] - level[num1]) + abs(level[root] - level[num2])

        
def search(T=0,flag=""):
    if flag == "전위":
        if T:
            print(T, end=" ")
            search(tree[T][left_child],"전위")
            search(tree[T][right_child],"전위")
    if flag == "중위":
        if T:
            search(tree[T][left_child],"중위")
            print(T, end=" ")
            search(tree[T][right_child],"중위")

    if flag == "후위":
        if T:
            search(tree[T][left_child],"후위")
            search(tree[T][right_child],"후위")
            print(T, end=" ")
    if flag == "레벨":
        for i in range(1,max(level)+1):
            print("레벨 {} :".format(i), end=" ")
            for j in range(len(level)):
                if level[j] == i:
                    print(j,end = ", ")
            print()

v= int(input())
e= v-1

tree = [ [0,0] for i in range(v*2) ]
n_child = [0] * (v+1)
parents = [0] * (v+1)
level = [0] * (v+1)
left_child = 0
right_child = 1

data = list(map(int,input().split()))
for i in range(e):
    parent = data[2*i]
    child = data[2*i+1]
    if tree[parent][left_child] == 0:
        tree[parent][left_child] = child
    elif tree[parent][right_child] == 0:
        tree[parent][right_child] = child

    parents[child] = parent
    level[child] = level[parent] + 1
    n_child[parent]+=1

print(tree)
search(1,"전위")
print()
search(1,"중위")
print()
search(1,"후위")
print()
search(flag="레벨")

print(dis(12,13))


