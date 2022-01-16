import difflib
from txt2Arr import toArr
from avl import AVL_Tree

def bruteForce(word):
    found = False
    newWord = word + "\n"
    newWord.lower()
    dictionary = open('dictionary.txt', 'r')
    dic = toArr(dictionary)
    for words in dic:
        words.lower
        if words == newWord:
            found = True
            break
    if found == False:
        word = autoCorrect(word, dic)
        bruteForce(word)
        
    return word

def doDecreasebyConstant(word):
    newWord = word + "\n"
    dictionary = open('dictionary.txt', 'r')
    dic = toArr(dictionary)
    dic.sort
    found = binarySearch(newWord, dic)
    if found == True:
        return word
    else:
        word = autoCorrect(word, dic)
        doDecreasebyConstant(word)
        return word

def binarySearch(x, arr): 
    l = 0
    r = len(arr) - 1
    while (l <= r): 
        m = (l + r) // 2 
        if (arr[m] == x): 
               return True
        elif (arr[m] < x): 
            l = m + 1
        else: 
            r = m - 1
    return False



def avl(word, tree, root):
    dictionary = open('dictionary.txt', 'r')
    dic = toArr(dictionary)
    
    myTree = tree
    myRoot = root

    newWord = word +"\n"
    
    if(myTree.search(myRoot, newWord)):
        print("would you like to use or delete this word")
        use= input("\"use\" or \"delete\"\n")
        if(use == "delete"):
            myTree.delete(myRoot, newWord)
            print("word deleted. game will begin with defult word")
            return "mango"
        elif(use == "use"):
            newWord= word
            return newWord
    else:
        print("Would you like to add to list?")
        add = input("\"yes\" or \"no\"\n")
        if(add== "yes"):
            myTree.insert(myRoot, newWord)
            newWord= word
            return newWord
        else:
            newWord = autoCorrect(word, dic)
            return newWord



def autoCorrect(word, arr):
    closest = difflib.get_close_matches(word, arr)
    print("sorry your word was not found. Did you mean:")
    for match in closest: 
        print(match)
    newWord = input("please type a word from the list\n")
    return newWord


