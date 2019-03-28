import sys
sys.stdin = open("퇴사.txt")
# #내가 일정을 시작할 수 있는 시작점은 day이다.
# #이 선택을 하였을때 현재까지 벌 수 있는 예상금액은 cnt이다.
# def DFS(day,cnt):
#     global myMax
#     #내가 고른 일정이 내 퇴사일 보다 넘어간다면 그 일정은 고를수 없다.
#     if day > N: return
#
#     #내가 지금까지 선택한 일정에서 벌어 들인 금액이
#     #이전에 선택했던 일정에서 최대로 벌 수 있는 금액보다 크기 때문에
#     #지금 선택한 일정에서 벌어드린 돈이 새로운 최대금액이다.
#     if cnt>myMax:
#         myMax = cnt
#
#     #내 일정이 끝나는 날부터 남은 일에서 하나를 고른다.
#     for i in range(day,N):
#         #내가 일정을 고르면(i) 그 일정으로부터 T일 이후부터 상담이 가능하다.(data[i][0])
#         #내가 일정을 고르면 내가 벌었던 금액은
#         #지금까지 벌었던 금액(cnt)에 상담비(data[i][1])를 더한 값이다.
#         DFS(i+data[i][0],cnt+data[i][1])
#
# N = int(input())
# data = []
# for i in range(N):
#     #상담일수와, 금액
#     T,P = map(int,input().split())
#     data.append((T,P))
# #내가 최대한 벌수 있는 돈
# myMax = 0
# #백트래킹
# DFS(0,0)
# print(myMax)

#내가 일정을 시작할 수 있는 시작점은 day이다.
#이 선택을 하였을때 현재까지 벌 수 있는 예상금액은 cnt이다.
def DFS(day,cnt):
    global myMax
    #내가 고른 일정이 내 퇴사일 보다 넘어간다면 그 일정은 고를수 없다.
    if day > N: return

    #내가 지금까지 선택한 일정에서 벌어 들인 금액이
    #이전에 선택했던 일정에서 최대로 벌 수 있는 금액보다 크기 때문에
    #지금 선택한 일정에서 벌어드린 돈이 새로운 최대금액이다.
    if cnt>myMax:
        myMax = cnt

    #내 일정이 끝나는 날부터 남은 일에서 하나를 고른다.
    for i in range(day,N):
        DFS(i+data[i][0],cnt+data[i][1])

N = int(input())
data = []
for i in range(N):
    #상담일수와, 금액
    T,P = map(int,input().split())
    data.append((T,P))
#내가 최대한 벌수 있는 돈
myMax = 0
#백트래킹
DFS(0,0)
print(myMax)


