
dic= {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'}

deco = {
    '001101':0,
    '010011':1,
    '111011':2,
    '110001':3,
    '100011':4,
    '110111':5,
    '001011':6,
    '111101':7,
    '011001':8,
    '101111':9}

def func(d,start):
    for j in range(start, start + 6):
        if data[j] != d[j-start]:
            return False
    return True

indata = ['0','2','6','9','F','A','C','9','A','0']
data = ''
for i in range(len(indata)):
    data+=dic[indata[i]]

start = 0
while start <= len(data)-6:

    flag = False
    for d in deco:
        if func(d,start):
            flag = True
            print(deco[d], end=" ")

    if flag:
        start+=6
    else :
        start+=1





