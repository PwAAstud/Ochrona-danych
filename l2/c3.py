from math import log2
from itertools import product
from string import ascii_lowercase

def RC4(key:list[bytes], outLen:int) -> list[int]:
    # Inicjalizowanie rejestru S:
    s = []
    for i in range(256): s.append(i)

    j = 0
    for i in range(256):
        j = (j + s[i] + key[i%len(key)])%256
        s[i], s[j] = s[j], s[i]

    # Generowanie strumienia klucza K
    i = 0
    j = 0

    k = []
    for i in range(outLen):
        i = (i+1)%256
        j = (j+s[i])%256
        s[i], s[j] = s[j], s[i]
        k.append(s[ (s[i]+s[j])%256 ])
    return k

def encode(data:list[bytes], key:list[bytes]):
    xorList = RC4(key, len(data))
    for i in range(len(data)):
        data[i] ^= xorList[i]

def z1():
    data = [2,6,1,7]
    key = [8,1]
    print(data)
    encode(data, key)
    print(data)
    encode(data, key)
    print(data)

def entropy(data:list[bytes]) -> float:
    count = [0 for i in range(256)]
    for d in data: count[d]+=1
    prob = [count[i]/len(data) for i in range(256)]
    ent = 0
    for p in prob:
        if(p==0): continue
        ent -= log2(p)*p
    return ent

def allKeys():
    litery = ascii_lowercase
    retList = []
    for l in [p for p in product(litery, repeat=3)]:
        l = list(l)
        for i in [0,1,2]: l[i] = ord(l[i])
        retList.append(l)
    return retList

def findKeyWithLowestEntropy():
    with open("rc4.bin", "rb") as f:
        data = list(f.read())

    data = data[:512]
    anserList = []
    for k in allKeys():
        dataC = data.copy()
        encode(dataC, k)
        ent = entropy(dataC)
        anserList.append((k, ent))

    anserList.sort(key= lambda x:x[1])
    for a in anserList[:5]:
        print(a[0], end=": ")
        print(a[1])
    return anserList[0][0]

z1()

print()

with open("rc4.bin", "rb") as f:
    data = list(f.read())

encode(data, findKeyWithLowestEntropy())
with open("rc4.txt", "wb") as f:
    f.write(bytes(data))