import sys
sys.stdin=open("정식이.txt","r")

def trans10(num,k):
    result = 0
    i = 0
    while num:
        result+=(num%10)*(k**i)
        num=num//10
        i+=1
    return result


for tc in range(int(input())):
    a = input()
    la = len(a)
    b = list(input())
    lb = len(b)
    a = trans10(int(a),2)



    for i in range(la):
        for j in range(lb):
            na = a ^ (1 << i)
            if b[j] == '0':
                b[j] = '1'
                nb = 0
                for k in range(lb):
                    nb+=int(b[k])*(3**(lb-k-1))
                if na == nb:
                    print("#{} {}".format(tc+1,na))
                    break

                b[j] = '2'
                nb = 0
                for k in range(lb):
                    nb += int(b[k]) * (3 ** (lb - k - 1))
                if na == nb:
                    print("#{} {}".format(tc + 1, na))
                    break
                b[j] = '0'

            elif b[j] == '1':
                b[j] = '0'
                nb = 0
                for k in range(lb):
                    nb += int(b[k]) * (3 ** (lb - k - 1))
                if na == nb:
                    print("#{} {}".format(tc + 1, na))
                    break

                b[j] = '2'
                nb = 0
                for k in range(lb):
                    nb += int(b[k]) * (3 ** (lb - k - 1))
                if na == nb:
                    print("#{} {}".format(tc + 1, na))
                    break
                b[j] = '1'

            else :
                b[j] = '0'
                nb = 0
                for k in range(lb):
                    nb += int(b[k]) * (3 ** (lb - k - 1))
                if na == nb:
                    print("#{} {}".format(tc + 1, na))
                    break

                b[j] = '1'
                nb = 0
                for k in range(lb):
                    nb += int(b[k]) * (3 ** (lb - k - 1))
                if na == nb:
                    print("#{} {}".format(tc + 1, na))
                    break
                b[j] = '2'