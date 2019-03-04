import sys
sys.stdin = open("KMP.txt","r")

def makePi(pattern) :
    piTable = [0] * len(pattern)
    j = 0
    for i in range(1,len(pattern)) :
        while pattern[i] != pattern[j] :
            if j == 0 :
                piTable[i] = j
                break
            j = piTable[j-1]
        if pattern[i] == pattern[j] :
            piTable[i] = j+1
            j+= 1
    return piTable

n = int(input())
item = input()
piTable = makePi(item)
print(piTable)
print(n-piTable[n-1])