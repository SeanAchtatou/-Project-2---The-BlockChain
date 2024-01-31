#SHA-256#
import hashlib
c = ""
a = ""
hash = (hashlib.sha256(a.encode()).hexdigest())
print(hash)
print(len(hash))
print()

a = 0
for i in range(1,10000000000000000):
    a += 1
    b = (hashlib.sha256(str(a).encode()).hexdigest())
    print("Number", i , "=" , b)
    print(b[:4])
    if b[:4] == "0000":
        if c == "":
            c = "Number",i,"=",b
            continue
        else:
            print(c)
            print("Number",i,"=",b)
            exit()





