def Merkle_Tree(a):
    import hashlib
    hash = 0
    j = 1
    dict = a
    n = 0
    p = len(dict)
    block = []
    while len(dict) > 1:
        if len(dict)%2 == 1:
            dict.append(hashlib.sha256(str(0).encode()).hexdigest())
            p +=1
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
                j += 1
                dict = block.copy()
                block.clear()
                p = n / 2
                n = 0
                if len(dict) > 1 and len(dict) % 2 == 1:
                    dict.append(hashlib.sha256(str(0).encode()).hexdigest())
                    p += 1
                else:
                    pass
    if dict == []:
        return hash
    else:
        return dict[0]

