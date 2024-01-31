#SHA-256 with MERKLE TREE#
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Merkle Tree Calculator")
print("#########################################################################################################")
print("# Project : Merkle Tree calculator based on the SHA-256 Hash Function for a random numbers of integers  #")
print("# Author : SEAN ACHTATOU                                                                                #")
print("# All Rights Reserved 2018                                                                              #")
print("#########################################################################################################")
print("")
import time
import random
import hashlib
while True:

    j = 1
    dict = []
    # Insert here you elements from where to where it is going to be hashed / it is a simple one !!!!! PLEASE ENTER NUMBER THAT ARE BASE 2 !!!!!!#
    p = int(input("Enter the numbers of elements in the Merkle Tree >"))
    print("")
    print("Top hash for the elements from:", p - (p - 1), "->", p)
    print("")
    for i in range(p):
        # number = random.randint(0,100)
        # hash = hashlib.sha256(str(number).encode()).hexdigest()
        hash = hashlib.sha256(str(i).encode()).hexdigest()
        print(i, "=", hash)
        dict.append(hash)
    print("")
    print("Here are the hashed data at the base of the Merkle Tree:")
    print(dict)
    verify = dict.copy()
    print("")
    n = 0
    block = []
    while len(dict) > 1:
        if len(dict) > 1 and len(dict) % 2 == 1:
            dict.append(hashlib.sha256(str(0).encode()).hexdigest())
            p += 1
            print("Add an hash of zeros.")
            print(dict)
        else:
            pass
        for _ in dict:
            if p > 1:
                sum = dict[n] + dict[n + 1]
                hash = hashlib.sha256(sum.encode()).hexdigest()
                block.append(hash)
                n += 2
                p -= 2
            else:
                print("After", j, "hashes:")
                j += 1
                print(block)
                dict = block.copy()
                block.clear()
                p = n / 2
                n = 0
                if len(dict) > 1 and len(dict) % 2 == 1:
                    dict.append(hashlib.sha256(str(0).encode()).hexdigest())
                    p += 1
                    print("Add an hash of zeros.")
                else:
                    pass
    print("")
    if dict == []:
        print("Top hash of the elements is :", hash)
    else:
        print("Top hash of the elements is:", dict)

    print("")




