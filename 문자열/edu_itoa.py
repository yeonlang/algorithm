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

print(type(result))
print(result)