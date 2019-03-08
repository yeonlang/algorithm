from itertools import product,combinations,permutations
# for i in combinations(range(1,4),2):
#     print(i)
k = 3
for i in set(permutations((0,1)*k,k)):
    print(i)