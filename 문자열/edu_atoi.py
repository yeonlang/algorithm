atoi=['4','2','F','B']
for i in range(len(atoi)):
    if '0'<= atoi[i] <= '9':
        atoi[i]=ord(atoi[i])-ord('0')
    elif 'A' <= atoi[i] <= 'F':
        atoi[i] = ord(atoi[i])-ord('A')+10


print(atoi)