from itertools import product,combinations,permutations
# for i in combinations(range(1,4),2):
#     print(i)
i =(1,)
print(len(i))
for v in product([i],set(combinations([1,0]*3,3))):
    print(v)

for t in combinations(range(4),1):
    print(t)