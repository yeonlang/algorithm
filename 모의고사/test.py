stack = [(0,0,1),(0,0,2),(3,3,1),(4,5,0)]
stack.sort(key=lambda x: x[2])
print(stack)