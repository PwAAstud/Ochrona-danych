def str2Key(s:str):
    keyI = [] 
    for c in s:
        keyI.append(ord(c))
    return keyI

def encode(key:str, file:str) -> None:
    if(len(key)==0): return
    keyI = str2Key(key)

    with open(file, "rb") as f:
        data = f.read()
    if(len(data)==0): return

    retData = []
    for i in range(len(data)):
        # data[i] = (data[i] + keyI[i%len(keyI)])%256
        retData.append((data[i] + keyI[i%len(keyI)])%256)

    with open("vigenere.bin", "wb") as f:
        f.write(bytes(retData))

def testEncoding(key:str) -> bool:
    keyI = str2Key(key)
    f1 = open("tekst_pl.txt", "rb")
    f2 = open("vigenere.bin", "rb")

    data1 = f1.read()
    data2 = f2.read()
    f1.close()
    f2.close()
    if(len(data1) != len(data2)): return False

    for i in range(len(data1)):
        if((data2[i] - keyI[i%len(keyI)])%256 != data1[i]):
            return False
    return True

key = "ZAMEK"
encode(key, "tekst_pl.txt")

print("czy można poprawnie dokodować tekst:")
print(testEncoding(key))
print()
# c .3
def aplayKey(text:str, key:str):
    keyI = str2Key(key)

    for i in range(len(text)):
        print((ord(text[i]) + keyI[i%len(keyI)])%256, end=" ")
    print("")

text = "BRAMABRAMABRAMA"
print("SZYFR")
aplayKey(text, "SZYFR")
print("KOD")
aplayKey(text, "KOD")