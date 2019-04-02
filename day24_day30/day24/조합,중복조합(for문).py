n = 5
r = 3

# 조합
for n1 in range(1,n+1):
    for n2 in range(n1+1,n+1):
        for n3 in range(n2+1,n+1):
            print(n1,n2,n3)

# 중복조합
# for n1 in range(1,n+1):
#     for n2 in range(n1,n+1):
#         for n3 in range(n2,n+1):
#             print(n1,n2,n3)
