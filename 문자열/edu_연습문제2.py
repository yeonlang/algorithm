atoi=['4','2','F','B']
for i in range(len(atoi)):
    if '0'<= atoi[i] <= '9':
        atoi[i]=ord(atoi[i])-ord('0')
    elif 'A' <= atoi[i] <= 'F':
        atoi[i] = ord(atoi[i])-ord('A')+10
print(atoi)

itoa=124
result = ''
temp=itoa%10
result=chr(temp+ord('0'))+result
i=1
while itoa//10**i:
    temp1=itoa//10**i
    temp=temp1%10
    result=chr(temp+ord('0'))+result
    i+=1

print(result)