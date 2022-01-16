import random
def arrAndGet(txtfile):
    arr = toArr("/Users/carlos/Downloads/hangman-master/dictionary.txt")
    return getRand(arr)


    
def getRand(arr):
    return random.choice(arr)


def toArr(txtfile):
    txtArr = []
    file = txtfile
    for line in file:
        txtArr.append(line)
    return txtArr


#print(arrAndGet("/Users/carlos/Downloads/hangman-master/dictionary.txt"))