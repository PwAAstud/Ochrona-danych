import sys

def howManyIsCarater(data:list[int], moveBy:int) -> int:
    retVal:int = 0
    for c in data:
        c = (c - moveBy) % 256
        if(32 <= c and c <= 126 or c in [9,10,13]):
            retVal += 1
    return retVal


with open("cezar.bin", "rb") as f:
# with open(sys.argv[1] , "rb") as f:
    data = f.read()
    # print(data)

option = []
for i in range(256):
    option.append((i, howManyIsCarater(data, i)/len(data)))

option.sort(key=lambda x: x[0])
option.sort(key=lambda x: x[1], reverse=True)

for a in option[:4]:
    print(f"psesuniece {a[0]}, procent dopasowań {a[1]}")
    for d in data[:100]:
        print(chr((d - a[0]) % 256), end="")
    print("\n---")

with open("cezar.txt", "wb") as f:
    data = [(d - 233) % 256 for d in data] # 233 z testu wynika
    f.write(bytes(data))