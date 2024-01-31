import json
import hashlib
import time
import Merkle_Tree_Function
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
t = 0
nbB = 6
Target = 5000

print("#####################################################################################")
print("# Project : Local Block Chain for BiCS BSP                                          #")
print("# Author : SEAN ACHTATOU                                                            #")
print("# All Rights Reserved 2018                                                          #")
print("#####################################################################################")
print("Please wait, the Block Chain is being created. This operation can take up to 30 seconds.")
print("")

class BlockChain : #Settings of the 5 block already in it#
    global Target

    unconfirmed = {}
    unconfirmed["Unconfirmed"] = []

    blocks = {}
    blocks["Blocks"] = []

    for i in range(nbB): # Create the blocks#
        block = {"Block" + " " + str(i): {"Height": i, "Hash": b, "Prev_Has": c, "Nonce": d, "MerkleRoot": e,"Txs":[]}}
        blocks["Blocks"].append(block)


    blocks["Blocks"][0]["Block 0"]["Txs"].append(hashlib.sha256("Test".encode()).hexdigest())
    blocks["Blocks"][0]["Block 0"]["Txs"].append(hashlib.sha256("Hello".encode()).hexdigest())
    blocks["Blocks"][0]["Block 0"]["Txs"].append(hashlib.sha256("World".encode()).hexdigest())

    blocks["Blocks"][1]["Block 1"]["Txs"].append(hashlib.sha256("Bye".encode()).hexdigest())
    blocks["Blocks"][1]["Block 1"]["Txs"].append(hashlib.sha256("Have fun".encode()).hexdigest())
    blocks["Blocks"][1]["Block 1"]["Txs"].append(hashlib.sha256("See you".encode()).hexdigest())

    blocks["Blocks"][2]["Block 2"]["Txs"].append(hashlib.sha256("This".encode()).hexdigest())
    blocks["Blocks"][2]["Block 2"]["Txs"].append(hashlib.sha256("is".encode()).hexdigest())
    blocks["Blocks"][2]["Block 2"]["Txs"].append(hashlib.sha256("sparta".encode()).hexdigest())

    blocks["Blocks"][3]["Block 3"]["Txs"].append(hashlib.sha256("I".encode()).hexdigest())
    blocks["Blocks"][3]["Block 3"]["Txs"].append(hashlib.sha256("am".encode()).hexdigest())
    blocks["Blocks"][3]["Block 3"]["Txs"].append(hashlib.sha256("groot".encode()).hexdigest())

    blocks["Blocks"][4]["Block 4"]["Txs"].append(hashlib.sha256("Hello".encode()).hexdigest())
    blocks["Blocks"][4]["Block 4"]["Txs"].append(hashlib.sha256("is it me".encode()).hexdigest())
    blocks["Blocks"][4]["Block 4"]["Txs"].append(hashlib.sha256("you looking for".encode()).hexdigest())

    blocks["Blocks"][5]["Block 5"]["Txs"].append(hashlib.sha256("It".encode()).hexdigest())
    blocks["Blocks"][5]["Block 5"]["Txs"].append(hashlib.sha256("doesn't work".encode()).hexdigest())
    blocks["Blocks"][5]["Block 5"]["Txs"].append(hashlib.sha256("that way".encode()).hexdigest())

    for i in range(nbB): #Merkle Tree of the block for the root#
        blocks["Blocks"][i]["Block" + " " + str(i)]["MerkleRoot"] = Merkle_Tree_Function.Merkle_Tree(blocks["Blocks"][i]["Block" + " " + str(i)]["Txs"])

    for i in range(nbB):  # Calculate the Hash and the Prev_Hash and the Nonce
        Cst = str(blocks["Blocks"][i]["Block" + " " + str(i)]["MerkleRoot"]) + str(blocks["Blocks"][i]["Block" + " " + str(i)]["Prev_Has"]) + str(blocks["Blocks"][i]["Block" + " " + str(i)]["Nonce"])
        Tcs = hashlib.sha256(Cst.encode()).hexdigest()
        Bts = abs(hash(Tcs))
        while Bts > Target:
            blocks["Blocks"][i]["Block" + " " + str(i)]["Nonce"] += 1
            Cst = str(blocks["Blocks"][i]["Block" + " " + str(i)]["MerkleRoot"]) + str(blocks["Blocks"][i]["Block" + " " + str(i)]["Prev_Has"]) + str(blocks["Blocks"][i]["Block" + " " + str(i)]["Nonce"])
            Tcs = hashlib.sha256(Cst.encode()).hexdigest()
            Bts = abs(hash(Tcs))
        blocks["Blocks"][i]["Block" + " " + str(i)]["Hash"] = Tcs
        if i < nbB-1:
            blocks["Blocks"][i+1]["Block" + " " + str(i+1)]["Prev_Has"] =  blocks["Blocks"][i]["Block" + " " + str(i)]["Hash"]
        else:
            continue


with open("data.txt", "w") as i:  # Put all the data in a data.txt file#
    json.dump(BlockChain.unconfirmed, i, indent=4)
    json.dump(BlockChain.blocks, i, indent=4)
    i.close()

########################################################################################################################

def New_Transaction_Unconfirmed(a):
   #Append a new transaction unconfirmed to the Unconfirmed#
   BlockChain.unconfirmed["Unconfirmed"].append(a)
   print("[Success] Your transaction has been add to the unconfirmed transactions.")

def Mine_Block():
    global nbB,Target

    for i in range(nbB): #Look in the unconfirmed if a transaction doesn't already exist in the blocks#
        for k in BlockChain.blocks["Blocks"][i]["Block" + " " + str(i)]["Txs"]:
            count = -1
            for j in BlockChain.unconfirmed["Unconfirmed"]:
                count += 1
                if k == j:
                    print("[Warning] An unconfirmed transaction contains a transaction already found in a block, this transaction is being deleted from the unconfirmed.")
                    del BlockChain.unconfirmed["Unconfirmed"][count]
                else:
                    continue
    if BlockChain.unconfirmed["Unconfirmed"] == []:
        print("[Error] No transactions in the Unconfirmed, no block has been created.")
    else:
        block = {"Block" + " " + str(nbB): {"Height": nbB, "Hash": b, "Prev_Has": c, "Nonce": d, "MerkleRoot": e, "Txs": []}}
        BlockChain.blocks["Blocks"].append(block)

        for i in BlockChain.unconfirmed["Unconfirmed"]:
            BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["Txs"].append(i)
        BlockChain.unconfirmed["Unconfirmed"] = []
        # Read previous block hash#
        BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["Prev_Has"] = BlockChain.blocks["Blocks"][nbB-1]["Block" + " " + str(nbB-1)]["Hash"]
        # Calculate MerkleRoot of transaction#
        BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["MerkleRoot"] = Merkle_Tree_Function.Merkle_Tree(BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["Txs"])
        # Find nounce#
        Cst = str(BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["MerkleRoot"]) + str(BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["Prev_Has"]) + str(BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["Nonce"])
        Tcs = hashlib.sha256(Cst.encode()).hexdigest()
        Bts = abs(hash(Tcs))
        while Bts > Target:
            BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["Nonce"] += 1
            Cst = str(BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["MerkleRoot"]) + str(BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["Prev_Has"]) + str(BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["Nonce"])
            Tcs = hashlib.sha256(Cst.encode()).hexdigest()
            Bts = abs(hash(Tcs))
            BlockChain.blocks["Blocks"][nbB]["Block" + " " + str(nbB)]["Hash"] = Tcs
        nbB +=1

def Search_Block_Contents(a):
    print("Informations for the Block",a,":")
    try:
        print(BlockChain.blocks["Blocks"][int(a)]["Block"+" "+a])
        print("[Success] The contents for the Block", an, "has been displayed.")
    except:
        print("[Error] The Block Height you entered doesn't exist.")
    #Read for each block the height, once found, print the block contents#
    return

def Search_Transaction_Hash_Block(a):
    for i in range(nbB):
        for k in BlockChain.blocks["Blocks"][i]["Block" + " " + str(i)]["Txs"]:
            if k == hashlib.sha256(a.encode()).hexdigest():
                print("[Success] Transaction found in the Block",i)
                print("Hash of the Block",i,":",BlockChain.blocks["Blocks"][i]["Block"+" "+str(i)]["Hash"])
                return
            else:
                continue
    print("[Error] The transaction hasn't been found in any Blocks.")
    return None

########################################################################################################################
while True:
    answer = input("What would like to do [AddTransaction : AT ,MineTransactions : MT ,GetBlockContents : GBC ,GetHashOfTransactionBlock : GHOTB ,Exit : EXIT ] ?  >").lower()
    if answer == "at":
        an = input("Enter the data to be put in a new unconfirmed transaction >")
        NewTran = hashlib.sha256(an.encode()).hexdigest()
        New_Transaction_Unconfirmed(NewTran)
    elif answer == "mt":
        print("Start of the Mining.")
        print("The unconfirmed Blocks are being Mined. Please wait.")
        Mine_Block()
        print("Mining terminated.")
    elif answer == "gbc":
        an = input("Enter the Block Height you are looking for >")
        Search_Block_Contents(an)
    elif answer == "ghotb":
        an = input("Enter the transaction you are looking for >")
        Search_Transaction_Hash_Block(an)
    elif answer == "exit":
        print("The Block Chain is shutting down.")
        with open("data.txt", "w") as i:  # Put all the data in a data.txt file#
            json.dump("The Block Chain is not running.",i)
            i.close()
        time.sleep(3)

        exit()
    else:
        print("[Error] Please enter a valid option.")
    print()
    with open("data.txt", "w") as i: #Put all the data in a data.txt file#
        json.dump(BlockChain.unconfirmed, i, indent=4)
        json.dump(BlockChain.blocks, i, indent=4)
        i.close()












